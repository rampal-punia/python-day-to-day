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

print(target_dir_dict)
# Move files to their respective target directories
for fl in source_dir.rglob('*'):
    if fl.is_file():
        target_path = target_dir_dict.get(fl.suffix[1:])
        if target_path:
            target_file_path = target_path / fl.name
            fl.rename(target_file_path)
