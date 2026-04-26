# 📁 Downloads Organizer

A Python script that automatically sorts your Downloads folder by file type, extension, and date — keeping things tidy without you lifting a finger.

---

## Folder Structure

After running, your Downloads folder will look like this:

```
Downloads/
├── Documents/
│   └── PDF/
│       └── 2025-04/
│           └── report.pdf
├── Images/
│   └── JPG/
│       └── 2025-03/
│           └── photo.jpg
├── Videos/
│   └── MP4/
│       └── 2025-04/
│           └── tutorial.mp4
├── Audio/
├── Archives/
├── Code/
├── Executables/
└── Other/         ← anything unrecognized
```

Each file is sorted into 3 levels: **Type → Extension → Month downloaded**

---

## How It Works

- Scans every file in your Downloads folder
- Looks up the file extension in a category map
- Reads the file's modification date to determine the month
- Moves it into the right folder, creating folders as needed
- If a file with the same name already exists, it renames it safely (`file_1.pdf`, `file_2.pdf`, …) instead of overwriting
- Skips hidden files and subfolders so already-organized files aren't touched
- Logs every action to `~/.downloads_organizer.log`

---

## File Categories

| Category    | Extensions                                              |
|-------------|--------------------------------------------------------|
| Images      | .jpg, .jpeg, .png, .gif, .webp, .svg, .heic            |
| Videos      | .mp4, .mkv, .avi, .mov, .webm                          |
| Audio       | .mp3, .wav, .aac, .flac, .m4a                          |
| Documents   | .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .txt, .csv |
| Archives    | .zip, .tar, .gz, .rar, .7z                             |
| Code        | .py, .js, .html, .css, .json, .sh                      |
| Executables | .exe, .dmg, .pkg, .deb, .apk                           |
| Other       | anything not in the list above                         |

---

## Usage

### Run manually

```bash
python organize_downloads.py
```

### Schedule it (Windows Task Scheduler)

1. Open **Task Scheduler** (`Win + S` → search Task Scheduler)
2. Click **Create Basic Task**
3. Name it `Downloads Organizer`
4. Set your preferred trigger (Daily recommended)
5. Action → **Start a program**
   - **Program/script:** `C:\Python314\python.exe`
   - **Arguments:** `C:\Users\YourName\path\to\organize_downloads.py`
6. Click **Finish**
7. Right-click the task → **Run** to test it

---

## Requirements

- Python
- No third-party libraries — uses only the standard library (`os`, `shutil`, `logging`, `pathlib`, `datetime`)

---

## Logs

Every run is logged to:

```
C:\Users\YourName\.downloads_organizer.log
```

A log entry looks like:

```
2025-04-26 09:00:01  INFO      Moved  report.pdf     →  Documents/PDF/2025-04/report.pdf
2025-04-26 09:00:01  INFO      Done. Moved: 12  |  Skipped: 3
```

---

## Customization

To add new file types, edit the `FILE_TYPE_MAP` dictionary at the top of the script:

```python
FILE_TYPE_MAP = {
    "Ebooks": [".epub", ".mobi"],   # ← add a new category like this
    ...
}
```

---