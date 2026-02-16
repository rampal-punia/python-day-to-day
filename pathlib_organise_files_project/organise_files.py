"""Organise Files by Extension — Sort files into folders using pathlib.

Difficulty: 🟡 Intermediate
Topics: pathlib, Path.rglob(), Path.rename(), file extensions, automation

This script scans a source directory, groups files by their extension,
creates target sub-directories (e.g., 'csv_files/', 'json_files/'),
and moves each file into its corresponding folder.

Author: @rampal-punia
"""

from pathlib import Path


def get_unique_extensions(source_dir: Path) -> set[str]:
    """Collect all unique file extensions in the source directory.

    Args:
        source_dir: Path to the source directory.

    Returns:
        Set of extension strings (without the leading dot).
    """
    return {fl.suffix[1:] for fl in source_dir.iterdir() if fl.is_file() and fl.suffix}


def create_target_dirs(target_base: Path, extensions: set[str]) -> dict[str, Path]:
    """Create a target sub-directory for each file extension.

    Args:
        target_base: Base directory for organized output.
        extensions: Set of file extensions to create folders for.

    Returns:
        Dict mapping extension to its target directory path.
    """
    ext_dirs: dict[str, Path] = {}
    for ext in extensions:
        target_dir = target_base / f"{ext}_files"
        target_dir.mkdir(parents=True, exist_ok=True)
        ext_dirs[ext] = target_dir
    return ext_dirs


def organise_files(source_dir: Path, target_base: Path) -> int:
    """Move files from source into extension-based sub-directories.

    Args:
        source_dir: Directory containing files to organise.
        target_base: Base directory for the organised output.

    Returns:
        Number of files moved.

    Raises:
        FileNotFoundError: If source_dir doesn't exist.
    """
    if not source_dir.is_dir():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    extensions = get_unique_extensions(source_dir)
    if not extensions:
        print("  No files found in source directory.")
        return 0

    print(f"  Extensions found: {sorted(extensions)}")
    ext_dirs = create_target_dirs(target_base, extensions)

    moved = 0
    for fl in source_dir.rglob("*"):
        if fl.is_file() and fl.suffix:
            ext = fl.suffix[1:]
            target_path = ext_dirs.get(ext)
            if target_path:
                dest = target_path / fl.name
                fl.rename(dest)
                print(f"  Moved: {fl.name} → {target_path.name}/")
                moved += 1

    return moved


if __name__ == "__main__":
    cwd = Path.cwd()
    source = cwd / "source copy"
    target = cwd / "target"

    print("── File Organiser ──")
    if source.is_dir():
        count = organise_files(source, target)
        print(f"\n  Total files moved: {count}")
    else:
        print(f"  Source directory not found: {source}")
        print("  Create a 'source copy' folder with files to organise.")
