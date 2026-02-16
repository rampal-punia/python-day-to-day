"""Change Image Format — Convert images between formats using Pillow.

Difficulty: 🟢 Easy
Topics: PIL/Pillow, Image.open(), Image.save(), format conversion
Requires: pip install Pillow

Author: @rampal-punia
"""

from pathlib import Path
from PIL import Image


def change_format(
    image_path: str | Path, output_format: str, output_dir: str | Path = "."
) -> Path:
    """Convert an image to a different format.

    Args:
        image_path: Path to the source image.
        output_format: Target format (e.g., 'png', 'bmp', 'webp').
        output_dir: Directory for the output file (default: current dir).

    Returns:
        Path to the converted image.

    Raises:
        FileNotFoundError: If the source image doesn't exist.
    """
    src = Path(image_path)
    if not src.is_file():
        raise FileNotFoundError(f"Image not found: {src}")

    image = Image.open(src)
    output_path = Path(output_dir) / f"{src.stem}.{output_format.lower()}"
    image.save(output_path)

    print(f"  ✅ Converted: {src.name} ({image.format}) → {output_path.name}")
    return output_path


if __name__ == "__main__":
    print("── Image Format Conversion ──")
    try:
        change_format("laptops.jpg", "png")
    except FileNotFoundError as e:
        print(f"  ⚠️ {e} — place an image named 'laptops.jpg' in this directory.")

# For more on Python follow: https://x.com/rs_punia_
