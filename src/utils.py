import os

def ensure_directory_exists(directory):
    """
    Ensure the directory exists; if not, create it.
    """
    os.makedirs(directory, exist_ok=True)
