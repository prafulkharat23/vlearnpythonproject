#Q4. In DevOps, performing regular backups of important files is crucial:
#Implement a Python script called backup.py that takes a source directory and a destination directory as command-line arguments.
#The script should copy all files from the source directory to the destination directory.
#Before copying, check if the destination directory already contains a file with the same name. If so, append a timestamp to the file name to ensure uniqueness.
#Handle errors gracefully, such as when the source directory or destination directory does not exist.
#Sample Command:
#python backup.py /path/to/source /path/to/destination
#By running the script with the appropriate source and destination directories, it should create backups of the files in the source directory, ensuring unique file names in the destination directory.

import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if source and destination directories exist
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    if not os.path.exists(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return

    # Iterate over each file in the source directory
    for file_name in os.listdir(source_dir):
        src_file = os.path.join(source_dir, file_name)

        # Skip subdirectories
        if not os.path.isfile(src_file):
            continue

        dest_file = os.path.join(dest_dir, file_name)

        # If file exists, append timestamp
        if os.path.exists(dest_file):
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            name, ext = os.path.splitext(file_name)
            new_file_name = f"{name}_{timestamp}{ext}"
            dest_file = os.path.join(dest_dir, new_file_name)

        try:
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {file_name} -> {dest_file}")
        except Exception as e:
            print(f"Error copying {file_name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)
