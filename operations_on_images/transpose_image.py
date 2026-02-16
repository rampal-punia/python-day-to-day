"""Transpose Image — Rotate/flip using Pillow's transpose method.

Difficulty: 🟢 Easy
Topics: PIL/Pillow, Image.transpose(), ROTATE_90/180/270, FLIP
Requires: pip install Pillow

Difference from rotate():
    transpose() performs exact 90° rotations and flips without interpolation.
    rotate() supports arbitrary angles but may introduce artifacts.

Author: @rampal-punia
"""

from pathlib import Path
from PIL import Image


def transpose_image(
    image_path: str | Path,
    operation: Image.Transpose,
    output_path: str | Path | None = None,
) -> Path:
    """Apply a transpose operation to an image.

    Args:
        image_path: Path to the source image.
        operation: One of Image.Transpose.ROTATE_90, ROTATE_180,
                   ROTATE_270, FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM.
        output_path: Path for the output (auto-generated if None).

    Returns:
        Path to the transposed image.

    Raises:
        FileNotFoundError: If the source image doesn't exist.
    """
    src = Path(image_path)
    if not src.is_file():
        raise FileNotFoundError(f"Image not found: {src}")

    image = Image.open(src)
    result = image.transpose(operation)

    if output_path is None:
        output_path = src.with_stem(f"{src.stem}_{operation.name.lower()}")
    output_path = Path(output_path)
    result.save(output_path)

    print(f"  ✅ {operation.name}: {src.name} → {output_path.name}")
    return output_path


if __name__ == "__main__":
    print("── Image Transpose Operations ──")
    try:
        transpose_image("laptops.jpg", Image.Transpose.ROTATE_90)
        transpose_image("laptops.jpg", Image.Transpose.ROTATE_180)
        transpose_image("laptops.jpg", Image.Transpose.ROTATE_270)
        transpose_image("laptops.jpg", Image.Transpose.FLIP_LEFT_RIGHT)
        transpose_image("laptops.jpg", Image.Transpose.FLIP_TOP_BOTTOM)
    except FileNotFoundError as e:
        print(f"  ⚠️ {e}")

# For more on Python follow: https://x.com/rs_punia_
