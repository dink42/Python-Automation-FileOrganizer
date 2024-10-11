import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt', '.docx', '.csv'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png'],
    "EXCECUTABLES": ['.exe', '.zip', '.msi', '.gz'],
    "CODE": ['.java', '.cs', '.go', '.cpp'],
    "WEB": ['.html', '.css', '.js', '.ts']
}


def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'


def organizeDirectory():  

    script_name = os.path.basename(__file__)  # Get script's filename
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()  

        # Check filename before renaming (exclude script)
        if filePath.name != script_name:
            filePath.rename(directoryPath.joinpath(filePath))


organizeDirectory()