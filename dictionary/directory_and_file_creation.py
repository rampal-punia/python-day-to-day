"""Directory & File Creation — Using pathlib for filesystem operations.

Difficulty: 🟢 Easy
Topics: pathlib, Path.mkdir(), Path.open(), file I/O, error handling

Note: This file demonstrates pathlib usage. It's placed in dictionary/
      for historical reasons but relates more to pathlib concepts.

Author: @rampal-punia
"""

from pathlib import Path


def create_directory(path: str | Path) -> bool:
    """Create a directory (including parent directories) if it doesn't exist.

    Args:
        path: The directory path to create.

    Returns:
        True if created, False if it already existed.

    Raises:
        OSError: If the directory cannot be created.
    """
    path_obj = Path(path)
    if path_obj.exists():
        print(f"  Directory already exists: {path_obj}")
        return False
    try:
        path_obj.mkdir(parents=True)
        print(f"  ✅ Directory created: {path_obj}")
        return True
    except OSError as e:
        print(f"  ❌ Error creating directory '{path_obj}': {e}")
        raise


def create_file(path: str | Path, content: str = "") -> bool:
    """Create a file with optional content. Does not overwrite existing files.

    Args:
        path: The file path to create.
        content: Text content to write (default: empty).

    Returns:
        True if created, False if it already existed.

    Raises:
        OSError: If the file cannot be created.
    """
    path_obj = Path(path)
    if path_obj.is_file():
        print(f"  File already exists: {path_obj}")
        return False
    try:
        # Ensure parent directory exists
        path_obj.parent.mkdir(parents=True, exist_ok=True)
        path_obj.write_text(content, encoding="utf-8")
        print(f"  ✅ File created: {path_obj} ({len(content)} chars)")
        return True
    except OSError as e:
        print(f"  ❌ Error creating file '{path_obj}': {e}")
        raise


if __name__ == "__main__":
    import tempfile

    # Use a temporary directory for safe demo (no hardcoded paths)
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp) / "demo_project"

        print("── Creating Directory Structure ──")
        create_directory(base / "src")
        create_directory(base / "tests")
        create_directory(base / "src")  # Already exists

        print("\n── Creating Files ──")
        create_file(base / "src" / "main.py", 'print("Hello World!")')
        create_file(base / "README.md", "# Demo Project\n")
        create_file(base / "src" / "main.py")  # Already exists

        print(f"\n── Final Structure of {base.name}/ ──")
        for item in sorted(base.rglob("*")):
            indent = "  " * (len(item.relative_to(base).parts) - 1)
            if item.is_dir():
                print(f"  {indent}📁 {item.name}/")
            else:
                print(f"  {indent}📄 {item.name}")
