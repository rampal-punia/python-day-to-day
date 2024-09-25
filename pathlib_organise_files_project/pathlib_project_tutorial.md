# Learn All Important Methods of pathlib module with Single Project

Read My Blog On [Medium.Com](https://medium.com/@mycodingmantras): [Learn All Important Methods of pathlib Module with Single Project](https://medium.com/@mycodingmantras/learn-all-important-methods-of-pathlib-module-with-single-project-eb60a2f03053)

The pathlib module is a powerful and easy-to-use module for working with file-system paths, folders, and files. We will use the Path class from pathlib to create and manipulate file paths.

## What are we going to build?

In this tutorial, we will explore how to use Python's pathlib module to move files to their respective target directories based on their file extensions.

Ok, Let me put it in simpler words.

We have a directory called source with different extension files.

So, we have `.txt`, `.xlsx`, `.csv`, `.json` and `.docx` files in the source directory. Our task is to dump all the files into their respective directory.

This means:
`.txt` files will go to the `txt_files` directory
`.xlsx` files will go to the `xlsx_files` directory
`.json` files will go to the `json_files` directory

so on so forth.

Before continuing to our project let have a quick overview of Path class.

## A Quick Introduction to Path class of pathlib module

[Pathlib](https://docs.python.org/3/library/pathlib.html) module was introduced in Python 3.4 with [PEP 428](https://peps.python.org/pep-0428/).

It is a part of the Python standard library that provides an object-oriented interface for working with file paths. It allows us to create, manipulate, and operate on file paths in a platform-agnostic way.

Before introduction to this module in Python, the obvious module to work with files was OS module, which by the way is still very handy for many useful tasks.

But for working with files OS module manipulates the files path as pure strings. Whereas the Pathlib module takes an object-oriented approach.

### All the Methods and Attributes Available On Path Object

To get all the methods and attributes available on the Path object we will use the built-in function `dir()`.

```python
print([item for item in dir(Path) if not item.startswith('_')])

# Output
['absolute', 'anchor', 'as_posix', 'as_uri', 'chmod', 'cwd', 'drive', 'exists', 'expanduser', 'glob', 'group', 'home', 'is_absolute', 'is_block_device', 'is_char_device', 'is_dir', 'is_fifo', 'is_file', 'is_mount', 'is_reserved', 'is_socket', 'is_symlink', 'iterdir', 'joinpath', 'lchmod', 'link_to', 'lstat', 'match', 'mkdir', 'name', 'open', 'owner', 'parent', 'parents', 'parts', 'read_bytes', 'read_text', 'relative_to', 'rename', 'replace', 'resolve', 'rglob', 'rmdir', 'root', 'samefile', 'stat', 'stem', 'suffix', 'suffixes', 'symlink_to', 'touch', 'unlink', 'with_name', 'with_suffix', 'write_bytes', 'write_text']
```

### Directory Paths Manipulation With Path Class

```python
# Get current working directory
cwd = Path.cwd()
print(cwd)  # /home/RS_Punia/working-with-files

# Get home directory
print(Path.home())  # /home/RS_Punia

# Make a new directory with the name 'demofiles'
path = Path.cwd() / "demofiles"
path.mkdir()

# Join path of cwd to a directory names 'files' 
cwd = Path.cwd()
req_dir = cwd / "files"
print(req_dir)  # /home/RS_Punia/working-with-files/files
```

### Files Path Manipulation With Path Class

```python
# Check if a file exists
file = Path('readme.md')
print(file.exists())        # True

# List all files & dirs in a directory
child_obj = req_dir.iterdir()
for child in child_obj:
    print(child)
# Output
/home/RS_Punia/working-with-files/files/titanic_data.csv
/home/RS_Punia/working-with-files/files/excels
/home/RS_Punia/working-with-files/files/file3.csv
/home/RS_Punia/working-with-files/files/file1.txt
/home/RS_Punia/working-with-files/files/file2.txt

# Get a file with specific extension from a directory
print(sorted(req_dir.glob('*.txt')))
# Output:
[PosixPath('/home/RS_Punia/working-with-files/files/file1.txt'), PosixPath('/home/RS_Punia/working-with-files/files/file2.txt')]
```

### Get Files MetaData

```python
# Access a file
file = Path.cwd() / "readme.md"

# get absolute path of the file
absolute_path = file.resolve()
print(absolute_path)
# Output: /home/RS_Punia/working-with-files/readme.md

# Get parent folder
print(absolute_path.parent)
# Output: /home/RS_Punia/working-with-files

# Get name of the file
print(file.name)
# Output: readme.md

# Get suffix
print(file.suffix)
# Output: .md

# Get stem
print(file.stem)
# Output: readme

# Get root
print(file.root)
# Output: /

# Get parts of the path
print(file.parts)
# Output: ('/', 'home', 'RS_Punia', 'working-with-files', 'readme.md')

# Create new file in current working directory
Path.touch((Path(".") / "new_file.md"))
# Or
Path.touch((Path.cwd() / "new_file.md"))

# Check Stat of this file
print(file.stat())
# Output
os.stat_result(st_mode=33188, st_ino=540055, st_dev=2080, st_nlink=1, st_uid=1000, st_gid=1000, st_size=1503, st_atime=1673239779, st_mtime=1673239779, st_ctime=1673239779)

# Access stat with key like
print(file.stat().st_size)      # 1503
print(file.stat().st_mtime)     # 1673239779.7524743
```

### Reading and Writing To Files

```python
# Read and Write to a file
file = Path('demo.txt')

# Create the file and write data
file.write_text("Hello demo file")

# read data from the file
print(file.read_text())
```

### Deleting A File and Directory

```python
# Remove a file
file = Path(".") / "new_file.md"
file.unlink()

# Remove a dir, Dir must be empty. (Still Be careful with this. Removes permanently.)
dir = Path(".") / "demodir"
dir.rmdir()
# If not empty the following error occurs
#  OSError: [Errno 39] Directory not empty:
```

### Building our project to Efficiently Organizing Files by Extension with Python's Pathlib Module

### Importing Required Modules

In this script, we will only use the `Path` class from the pathlib module.

```python
from pathlib import Path
```

### Setting the Source and Target Directories

In this script, we assume that there is a source directory and a target directory, both of which are located in the current working directory. We set the source directory to 'source' and the target directory to 'target'.

```python
# Current working directory
cwd = Path.cwd()

# Set the source and target directories
source_dir = cwd / "source"
target_base_dir = cwd / "target"
```

### Creating Respective Directories

We create a function to create the respective directories.

```python
def create_target_dir(target_base_dir, dir_name="test_dir"):
    """Create the respective directory if it does not exist"""
    target_dir = target_base_dir / dir_name
    target_dir.mkdir(parents=True, exist_ok=True)
    return target_dir
```

This function takes the target base directory and the directory name as arguments. It first creates a Path object for the target directory by joining the target base directory and the directory name. If the directory does not exist, it creates the directory using the `mkdir()` method of the Path class.

### Getting the Available File Extensions

We get all available file extensions inside the source directory using a set comprehension.

```python
# Get all available files extensions inside the source directory
file_exts = {fl.suffix[1:] for fl in source_dir.iterdir() if fl.is_file()}
```

We iterate over all files in the source directory using the `iterdir()` method of the Path class. We use the `is_file()` method to check if each item in the iteration is a file.

If it is a file, we use the suffix attribute to get its file extension, remove the dot prefix, and add it to the set of available file extensions.

### Storing Target Directories for Each File Extension in a Dictionary

We create a dictionary of target directories for each file extension.

```python
target_dir_dict = {
    file_ext: create_target_dir(target_base_dir, f"{file_ext}_files")
    for file_ext in file_exts
}
```

We use a dictionary comprehension to create a key-value pair for each file extension and its corresponding target directory. We call the `create_target_dir()` function for each file extension and assign the returned value to the key.

### Moving Files to Respective Target Directories

We move each file to its respective target directory.

```python
# Move files to their respective target directories
for fl in source_dir.rglob('*'):
    if fl.is_file():
        target_path = target_dir_dict.get(fl.suffix[1:])
        if target_path:
            target_file_path = target_path / fl.name
            fl.rename(target_file_path)
```

We use the `rglob()` method of the Path class to iterate over all files in the source directory and its subdirectories.

We use the `is_file()` method to check if each item in the iteration is a file. We then get the target directory for the file extension using the dictionary of target directories.

We create a target file path by joining the target directory and the file name. Finally, we move the file to the target file path using the `rename()` method of the Path class.

### Complete code

```python
from pathlib import Path

# Current working directory
cwd = Path.cwd()

# Set the source and target directories
source_dir = cwd / "source"
target_base_dir = cwd / "target"


def create_target_dir(target_base_dir, dir_name="test_dir"):
    """Create the target directory if it does not exist"""
    target_dir = target_base_dir / dir_name
    target_dir.mkdir(parents=True, exist_ok=True)
    return target_dir


# Get all available files extensions inside the source directory
file_exts = {fl.suffix[1:] for fl in source_dir.iterdir() if fl.is_file()}

target_dir_dict = {
    file_ext: create_target_dir(target_base_dir, f"{file_ext}_files")
    for file_ext in file_exts
}


# Move files to their respective target directories
for fl in source_dir.rglob('*'):
    if fl.is_file():
        target_path = target_dir_dict.get(fl.suffix[1:])
        if target_path:
            target_file_path = target_path / fl.name
            fl.rename(target_file_path)
```

### Conclusion

In this tutorial, we have learned how to use Python's pathlib module to move files to their respective target directories based on their file extensions.

We have used the `Path` class to create and manipulate file paths, the `mkdir()` method to create directories, and the `rename()` method to move files. By following the steps outlined in this tutorial, you should be able to create a script that can organize files based on their file extensions with ease.

### About the Author

Hi there! I'm RS Punia, a passionate Python software programmer with a keen interest in computer vision, artificial intelligence, and machine learning. I enjoy analyzing and visualizing data and building projects with Django and React. In addition to my programming skills, I also enjoy sharing my knowledge with others via social media. I often share about Python fundamentals, Quizzes, Machine Learning, and AI, as well as object detection & tracking algorithms. My programming journey began in 2011 with HTML, CSS, jQuery, and JavaScript, but I later shifted to C and C# before finally settling on Python in 2016. With my diverse skillset and passion for learning, I strive to contribute to the programming community and help others grow in their own programming journeys.
