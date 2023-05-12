import os
import glob

def cleanup():
    pattern = 'data*.json'
    files_to_remove = glob.glob(pattern)

    for file in files_to_remove:
        try:
            os.remove(file)
            print(f"Deleted file: {file}")
        except OSError as e:
            print(f"Error deleting file: {file}, reason: {e}")
