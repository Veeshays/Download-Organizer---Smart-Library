from datetime import datetime
from config import LOGFILE


def log(message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = f"[{timestamp}] {message}"

    print(line)

    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")