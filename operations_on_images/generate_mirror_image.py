"""Generate Mirror Image — Flip an image horizontally using Pillow.

Difficulty: 🟢 Easy
Topics: PIL/Pillow, ImageOps.mirror(), horizontal flip
Requires: pip install Pillow

Author: @rampal-punia
"""

from pathlib import Path
from PIL import Image, ImageOps


def mirror_image(image_path: str | Path, output_path: str | Path | None = None) -> Path:
    """Create a horizontally mirrored version of an image.

    Args:
        image_path: Path to the source image.
        output_path: Path for the output (auto-generated if None).

    Returns:
        Path to the mirrored image file.

    Raises:
        FileNotFoundError: If the source image doesn't exist.
    """
    src = Path(image_path)
    if not src.is_file():
        raise FileNotFoundError(f"Image not found: {src}")

    image = Image.open(src)
    mirrored = ImageOps.mirror(image)

    if output_path is None:
        output_path = src.with_stem(f"{src.stem}_mirrored")
    output_path = Path(output_path)
    mirrored.save(output_path)

    print(f"  ✅ Mirrored image saved: {output_path.name}")
    return output_path


if __name__ == "__main__":
    print("── Mirror Image Generation ──")
    try:
        mirror_image("laptops.jpg")
    except FileNotFoundError as e:
        print(f"  ⚠️ {e}")

# For more on Python follow: https://x.com/rs_punia_
