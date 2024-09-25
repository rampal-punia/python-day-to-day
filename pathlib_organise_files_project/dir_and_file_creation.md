# Using Pathlib module create a dir and file at given path

Functions for creating a new directory and a new file at a given path using Path from the pathlib module:

```python
from pathlib import Path

def create_directory(path: str) -> None:
    """
    Creates a new directory at the given path, if it doesn't already exist.
    """
    path = Path(path)
    if not path.is_dir():
        path.mkdir(parents=True)

def create_file(path: str, content: str = '') -> None:
    """
    Creates a new file at the given path, if it doesn't already exist.
    If content is provided, it writes the content to the file.
    """
    path = Path(path)
    if not path.is_file():
        with path.open(mode='w') as file:
            file.write(content)
```

The create_directory function takes a path as an argument and creates a new directory at that path using pathlib.Path.mkdir method. The parents=True argument allows the creation of any necessary intermediate directories. If the directory already exists, the function does nothing.

The create_file function takes a path as an argument and creates a new file at that path using pathlib.Path.open method with mode 'w' (write mode). If the file already exists, the function does nothing. If the optional content argument is provided, it writes the content to the file using the file.write method.

Note that these functions only create a single directory or file. If you want to create multiple directories or files at once, you can modify these functions to accept a list of paths instead.
