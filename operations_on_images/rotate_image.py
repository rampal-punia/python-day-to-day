"""Rotate Image — Rotate images by any angle using Pillow.

Difficulty: 🟢 Easy
Topics: PIL/Pillow, Image.rotate(), expand parameter, angle
Requires: pip install Pillow

Author: @rampal-punia
"""

from pathlib import Path
from PIL import Image


def rotate_image(
    image_path: str | Path,
    angle: int = 45,
    expand: bool = True,
    output_path: str | Path | None = None,
) -> Path:
    """Rotate an image by a given angle.

    Args:
        image_path: Path to the source image.
        angle: Rotation angle in degrees (counter-clockwise).
        expand: If True, expand the output to fit the full rotated image.
        output_path: Path for the output (auto-generated if None).

    Returns:
        Path to the rotated image file.

    Raises:
        FileNotFoundError: If the source image doesn't exist.
    """
    src = Path(image_path)
    if not src.is_file():
        raise FileNotFoundError(f"Image not found: {src}")

    image = Image.open(src)
    rotated = image.rotate(angle, expand=expand)

    if output_path is None:
        output_path = src.with_stem(f"{src.stem}_rotated_{angle}")
    output_path = Path(output_path)
    rotated.save(output_path)

    print(f"  ✅ Rotated {angle}°: {src.name} → {output_path.name}")
    return output_path


if __name__ == "__main__":
    print("── Image Rotation ──")
    try:
        rotate_image("laptops.jpg", angle=45)
        rotate_image("laptops.jpg", angle=90)
        rotate_image("laptops.jpg", angle=180)
    except FileNotFoundError as e:
        print(f"  ⚠️ {e}")

# For more on Python follow: https://x.com/rs_punia_
