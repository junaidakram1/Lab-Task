import os
import sys

def search_file(directory, file_name):
    """
    Recursively searches for a specified file within a directory and its subdirectories.

    Parameters:
        directory (str): The path of the directory to search.
        file_name (str): The name of the file to search for.

    Returns:
        bool: True if the file is found, False otherwise.
    """
    try:
        for root, dirs, files in os.walk(directory):
            if file_name in files:
                print(f"File found at: {os.path.join(root, file_name)}")
                return True
        print("File not found.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    if len(sys.argv) != 3:
        print("Usage: python file_search.py <directory> <filename>")
        return

    directory_path = sys.argv[1]
    file_name = sys.argv[2]

    if not os.path.isdir(directory_path):
        print(f"Invalid directory path: {directory_path}")
        return

    search_file(directory_path, file_name)

if __name__ == "__main__":
    main()
