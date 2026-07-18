import shutil

from config import CATEGORIES
from config import PROJECT_FOLDER

from logger import log


def move_file(file_path):

    if not file_path.exists():
        return

    extension = file_path.suffix.lower()

    folder = CATEGORIES.get(extension, "Others")

    destination_folder = PROJECT_FOLDER / folder

    destination_folder.mkdir(exist_ok=True)

    if file_path.parent == destination_folder:
        return

    destination = destination_folder / file_path.name

    counter = 1

    while destination.exists():

        destination = destination_folder / f"{file_path.stem}_{counter}{file_path.suffix}"

        counter += 1

    try:

        shutil.move(str(file_path), str(destination))

        log(f"Moved {file_path.name} → {folder}")

    except Exception as e:

        log(f"Move Failed : {e}")