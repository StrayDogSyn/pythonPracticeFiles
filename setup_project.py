import os
import shutil
from pathlib import Path

def cleanup_project():
    # Project root directory
    root_dir = Path(__file__).parent

    # Create new directory structure if it doesn't exist
    new_dirs = [
        'src',
        'src/common',
        'src/week1',
        'src/week2',
        'tests',
        'docs',
        'assets',
        '.venv'  # Single virtual environment directory
    ]
    
    for dir_path in new_dirs:
        (root_dir / dir_path).mkdir(parents=True, exist_ok=True)

    # Files to move from pythonPracticeFiles to src
    moves = [
        ('pythonPracticeFiles/code_w1', 'src/week1'),
        ('pythonPracticeFiles/code_w2', 'src/week2'),
        ('pythonPracticeFiles/assets', 'assets'),
    ]

    # Perform moves
    for source, dest in moves:
        source_path = root_dir / source
        dest_path = root_dir / dest
        if source_path.exists():
            # Move files from source to destination
            for item in source_path.glob('*'):
                if item.is_file():
                    shutil.copy2(item, dest_path)
                    print(f"Moved {item} to {dest_path}")

    # Cleanup redundant directories
    dirs_to_remove = [
        'source',  # Old venv directory
        'weather',  # Old venv directory
        'pythonPracticeFiles',  # Since we moved contents
    ]

    for dir_to_remove in dirs_to_remove:
        dir_path = root_dir / dir_to_remove
        if dir_path.exists():
            try:
                shutil.rmtree(dir_path)
                print(f"Removed {dir_to_remove}")
            except Exception as e:
                print(f"Could not remove {dir_to_remove}: {e}")

    # Consolidate JSON testing files
    examples_json = root_dir / 'examples' / 'json_testing.json'
    root_json = root_dir / 'json_testing.json'
    if examples_json.exists() and root_json.exists():
        # Keep the root version and remove the example version
        examples_json.unlink()
        print("Removed duplicate JSON testing file")

if __name__ == '__main__':
    cleanup_project()