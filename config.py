from pathlib import Path
import os

# ===================================================
# PROJECT FOLDER (Visible to user)
# ===================================================

HOME = Path.home()

PROJECT_FOLDER = HOME / "Smart Liberary"
PROJECT_FOLDER.mkdir(exist_ok=True)

# ===================================================
# WINDOWS APPDATA (Hidden application data)
# ===================================================

APPDATA_FOLDER = Path(os.getenv("LOCALAPPDATA")) / "Smart Liberary"
APPDATA_FOLDER.mkdir(exist_ok=True)

# ===================================================
# WATCHED FOLDER
# ===================================================

DOWNLOADS = PROJECT_FOLDER

# ===================================================
# LOG FILE
# ===================================================

LOGFILE = APPDATA_FOLDER / "download_log.txt"

# ===================================================
# CATEGORY FOLDERS
# ===================================================

CATEGORIES = {

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",

    ".pdf": "PDFs",

    ".doc": "Documents",
    ".docx": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",

    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",

    ".mp3": "Music",
    ".wav": "Music",

    ".exe": "Programs",

    ".py": "Python",

    ".txt": "Text"
}

# Create all category folders automatically
for folder in set(CATEGORIES.values()):
    (PROJECT_FOLDER / folder).mkdir(exist_ok=True)

(PROJECT_FOLDER / "Others").mkdir(exist_ok=True)