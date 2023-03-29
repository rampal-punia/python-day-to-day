'''✨ Python: Create Dir and File At Given Path Using pathlib module.✨'''

from pathlib import Path


def create_directory(path: str) -> None:
    """
    Creates a new directory at the given path, if it doesn't already exist.
    """
    path_obj = Path(path)
    if not path_obj.exists():
        try:
            path_obj.mkdir(parents=True)
            print(f"Directory created at {path}")
        except OSError as e:
            print(f"Error creating directory at {path}: {e}")


def create_file(path: str, content: str = '') -> None:
    """
    Creates a new file at the given path, if it doesn't already exist.
    If content is provided, it writes the content to the file.
    """
    path_obj = Path(path)
    try:
        if not path_obj.is_file():
            with path_obj.open(mode='w') as file:
                file.write(content)
                print(f"File created at {path}")
        else:
            print(f"File already exists at {path}")
    except OSError as e:
        print(f"Error creating file at {path}: {e}")


# create a new folder 'test-folder' on the path
# create_directory(path="/path/to/test-folder")
# create a new file 'test.py' and add content to it.
create_file(path='/home/ram/CodingMantras/python-day-to-day/local_folder/test-folder',
            content='print("Hello World!")')
