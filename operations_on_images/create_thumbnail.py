"""Create Thumbnail — Generate image thumbnails using Pillow.

Difficulty: 🟢 Easy
Topics: PIL/Pillow, Image.thumbnail(), aspect ratio preservation
Requires: pip install Pillow

Note: thumbnail() modifies the image IN PLACE and preserves aspect ratio.
The size parameter is a maximum bounding box, not exact dimensions.

Author: @rampal-punia
"""

from pathlib import Path
from PIL import Image


def create_thumbnail(
    image_path: str | Path,
    size: tuple[int, int] = (128, 128),
    output_dir: str | Path = ".",
) -> Path:
    """Create a thumbnail of an image.

    Args:
        image_path: Path to the source image.
        size: Maximum (width, height) for the thumbnail.
        output_dir: Directory for the output file.

    Returns:
        Path to the saved thumbnail.

    Raises:
        FileNotFoundError: If the source image doesn't exist.
    """
    src = Path(image_path)
    if not src.is_file():
        raise FileNotFoundError(f"Image not found: {src}")

    image = Image.open(src)
    original_size = image.size

    image.thumbnail(size)  # Modifies in place, preserves aspect ratio

    output_path = Path(output_dir) / f"thumbnail_{size[0]}x{size[1]}_{src.name}"
    image.save(output_path)

    print(f"  ✅ Thumbnail: {original_size} → {image.size} saved to {output_path.name}")
    return output_path


if __name__ == "__main__":
    print("── Thumbnail Creation ──")
    try:
        create_thumbnail("laptops.jpg", size=(128, 128))
        create_thumbnail("laptops.jpg", size=(64, 64))
    except FileNotFoundError as e:
        print(f"  ⚠️ {e}")

# For more on Python follow: https://x.com/rs_punia_
