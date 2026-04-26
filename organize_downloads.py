import os
import shutil
import logging
from pathlib import Path
from datetime import datetime

DOWNLOADS_DIR = Path.home() / "Downloads"

FILE_TYPE_MAP = {
    "Images":      [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".heic"],
    "Videos":      [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Audio":       [".mp3", ".wav", ".aac", ".flac", ".m4a"],
    "Documents":   [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"],
    "Archives":    [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code":        [".py", ".js", ".html", ".css", ".json", ".sh"],
    "Executables": [".exe", ".dmg", ".pkg", ".deb", ".apk"],
}

LOG_FILE = Path.home() / ".downloads_organizer.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)

log = logging.getLogger(__name__)

def get_file_type(suffix: str) -> str:
    suffix = suffix.lower()
    for category, extensions in FILE_TYPE_MAP.items():
        if suffix in extensions:
            return category
    return "Other"

def get_date_folder(file_path: Path) -> str:
    mtime = file_path.stat().st_mtime
    dt = datetime.fromtimestamp(mtime)
    return dt.strftime("%Y-%m")

def unique_destination(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suffix = dest.stem, dest.suffix
    counter = 1
    while True:
        candidate = dest.parent / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1

def organize():
    if not DOWNLOADS_DIR.exists():
        log.error("Downloads folder not found: %s", DOWNLOADS_DIR)
        return

    moved = 0
    skipped = 0

    for item in DOWNLOADS_DIR.iterdir():
        if item.name.startswith(".") or item.is_dir():
            skipped += 1
            continue

        suffix      = item.suffix
        file_type   = get_file_type(suffix)
        ext_folder  = suffix.lstrip(".").upper() or "NO_EXT"
        date_folder = get_date_folder(item)

        dest_dir = DOWNLOADS_DIR / file_type / ext_folder / date_folder
        dest_dir.mkdir(parents=True, exist_ok=True)

        dest = unique_destination(dest_dir / item.name)

        try:
            shutil.move(str(item), str(dest))
            log.info("Moved  %-40s  →  %s", item.name, dest.relative_to(DOWNLOADS_DIR))
            moved += 1
        except Exception as exc:
            log.error("Failed to move %s: %s", item.name, exc)

    log.info("Done. Moved: %d  |  Skipped: %d", moved, skipped)
