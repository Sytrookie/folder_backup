import os
import datetime
import py7zr

# Define the source folder and backup folder
src_folder = (
    "C:\\Folder\\Folder"  # Replace with the actual path to the 7DaysSaves folder
)
backup_folder = (
    "C:\\Folder\\FolderBackups"  # Replace with the actual path to the backup folder
)
backup_prefix = "Backup_"


def create_backup(src_folder, backup_folder):
    # Get the current date and time for the backup file name
    current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create the backup file path
    backup_file = os.path.join(backup_folder, backup_prefix + f"{current_date}.7z")

    print(f"Starting backup of {src_folder} to {backup_file}")

    # Create a 7z archive
    with py7zr.SevenZipFile(
        backup_file, "w", filters=[{"id": py7zr.FILTER_LZMA2, "preset": 1}]
    ) as archive:
        for root, _, files in os.walk(src_folder):
            for file in files:
                file_path = os.path.join(root, file)
                archive.write(file_path, os.path.relpath(file_path, src_folder))
                print(f"Adding {file_path} to archive")

    print(f"Backup completed: {backup_file}")


# Ensure the backup folder exists
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# Run the backup
create_backup(src_folder, backup_folder)
