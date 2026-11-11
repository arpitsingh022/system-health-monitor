
from pathlib import Path


class FileManager:

    @staticmethod
    def run(directory):

        path = Path(directory)

        if not path.is_dir():
            raise ValueError("Invalid directory")

        print("\n===== FILE INVENTORY =====")

        total_files = 0
        total_dirs = 0
        total_size = 0

        for item in path.rglob("*"):

            if item.is_file():

                total_files += 1
                total_size += item.stat().st_size

            elif item.is_dir():

                total_dirs += 1

        print("Total Files:", total_files)
        print("Total Directories:", total_dirs)
        print(f"Total Size: {total_size / (1024**2):.2f} MB")
