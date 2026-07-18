import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler

from config import DOWNLOADS

from organizer import move_file
from logger import log


# Temporary download extensions
IGNORE_EXTENSIONS = {
    ".crdownload",
    ".tmp",
    ".part"
}


class DownloadHandler(FileSystemEventHandler):

    def __init__(self):

        super().__init__()

        # Files we've already processed
        self.processed = set()

    # ----------------------------------------
    # Called whenever ANYTHING changes
    # ----------------------------------------

    def on_any_event(self, event):

        self.scan_folder()

    # ----------------------------------------

    def scan_folder(self):

        for file in DOWNLOADS.iterdir():

            if file.is_dir():
                continue
            # Skip hidden files/folders if any
            if file.name.startswith("."):
                continue

            # Ignore log file
            if file.name == "download_log.txt":
                continue

            # Ignore temporary browser downloads
            if file.suffix.lower() in IGNORE_EXTENSIONS:
                continue

            # Already moved?
            if str(file) in self.processed:
                continue

            # Wait until file is free
            if not self.file_ready(file):
                continue

            log(f"New completed file : {file.name}")
            # Ignore files already inside category folders
            if file.parent != DOWNLOADS:
                continue
            move_file(file)

            self.processed.add(str(file))

    # ----------------------------------------

    def file_ready(self, file):

        try:

            # Try opening file.
            # If Windows says "busy",
            # we'll wait until next event.
            with open(file, "rb"):
                return True

        except Exception:

            return False