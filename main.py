import time

from watchdog.observers import Observer

from config import DOWNLOADS

from watcher import DownloadHandler


def main():

    observer = Observer()

    observer.schedule(
        DownloadHandler(),
        str(DOWNLOADS),
        recursive=False
    )

    observer.start()

    print("=" * 50)
    print("Download Analyzer Running")
    print("=" * 50)
    print("Watching:", DOWNLOADS)

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()


if __name__ == "__main__":

    main()