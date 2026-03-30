import os
import shutil
from pathlib import Path
from collections import defaultdict

def organize_files(directory="."):
    """
    Organize files in a directory by file type.
    Creates subdirectories for different file categories.
    """
    path = Path(directory)

    # Define file categories
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.m4a', '.wma'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.go'],
    }

    # Create category directories if they don't exist
    for category in categories:
        category_path = path / category
        category_path.mkdir(exist_ok=True)

    # Move files to appropriate directories
    for file in path.iterdir():
        if file.is_file():
            file_ext = file.suffix.lower()

            # Find matching category
            moved = False
            for category, extensions in categories.items():
                if file_ext in extensions:
                    shutil.move(str(file), str(path / category / file.name))
                    print(f"Moved: {file.name} -> {category}/")
                    moved = True
                    break

            if not moved:
                # Move unorganized files to 'Other'
                other_path = path / 'Other'
                other_path.mkdir(exist_ok=True)
                shutil.move(str(file), str(other_path / file.name))
                print(f"Moved: {file.name} -> Other/")

if __name__ == "__main__":
    organize_files()
    print("\n✓ File organization complete!")
