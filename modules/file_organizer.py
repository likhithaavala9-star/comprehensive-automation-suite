import os
import shutil
import logging
import time
from datetime import datetime

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from automation_suite.config import WATCH_FOLDER, ORGANIZED_FOLDER, FILE_CATEGORIES
from automation_suite.utils import setup_logging


setup_logging()


class FileOrganizer(FileSystemEventHandler):

    def __init__(self, watch_folder=WATCH_FOLDER, organized_folder=ORGANIZED_FOLDER):
        super().__init__()

        self.watch_folder = watch_folder
        self.organized_folder = organized_folder

        self.stats = {
            'organized': 0,
            'duplicates': 0
        }

        self.file_categories = FILE_CATEGORIES
        self.observer = Observer()

        # Create folders
        os.makedirs(self.organized_folder, exist_ok=True)
        for folder in self.file_categories:
            os.makedirs(os.path.join(self.organized_folder, folder), exist_ok=True)
        os.makedirs(os.path.join(self.organized_folder, 'Others'), exist_ok=True)

    # ✅ START method (NEW)
    def start(self):
        self.observer.schedule(self, self.watch_folder, recursive=False)
        self.observer.start()
        logging.info(f"Started watching: {self.watch_folder}")

    # ✅ STOP method (NEW)
    def stop(self):
        self.observer.stop()
        self.observer.join()
        logging.info("Stopped watching.")

    def on_created(self, event):
        if event.is_directory:
            return

        logging.info(f"Detected new file: {event.src_path}")
        time.sleep(1)
        self.organize_file(event.src_path)

    def organize_file(self, file_path):
        if not os.path.exists(file_path):
            return

        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)
        ext = ext.lower()

        for category, extensions in self.file_categories.items():
            if ext in extensions:
                dest_folder = os.path.join(self.organized_folder, category)
                dest_path = os.path.join(dest_folder, filename)

                if os.path.exists(dest_path):
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    new_filename = f"{name}_{timestamp}{ext}"
                    dest_path = os.path.join(dest_folder, new_filename)
                    self.stats['duplicates'] += 1
                    logging.info(f"Duplicate found. Renamed to {new_filename}")

                shutil.move(file_path, dest_path)
                self.stats['organized'] += 1
                logging.info(f"Moved {filename} to {category}")
                return

        # Others
        dest_folder = os.path.join(self.organized_folder, 'Others')
        dest_path = os.path.join(dest_folder, filename)

        if os.path.exists(dest_path):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_filename = f"{name}_{timestamp}{ext}"
            dest_path = os.path.join(dest_folder, new_filename)
            self.stats['duplicates'] += 1
            logging.info(f"Duplicate found. Renamed to {new_filename}")

        shutil.move(file_path, dest_path)
        self.stats['organized'] += 1
        logging.info(f"Moved {filename} to Others")


# ✅ Standalone mode still works
if __name__ == "__main__":
    organizer = FileOrganizer()
    organizer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        organizer.stop()
