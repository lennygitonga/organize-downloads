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