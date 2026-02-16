"""Resize Image — Resize images to specific dimensions using OpenCV.

Difficulty: 🟢 Easy
Topics: OpenCV, cv2.resize(), aspect ratio, interpolation
Requires: pip install opencv-python

Author: @rampal-punia
"""

from pathlib import Path
import cv2


def resize_image(
    image_path: str | Path,
    width: int = 400,
    height: int = 250,
    output_path: str | Path | None = None,
) -> None:
    """Resize an image to the specified dimensions.

    Args:
        image_path: Path to the source image.
        width: Target width in pixels.
        height: Target height in pixels.
        output_path: Optional path to save the resized image.

    Raises:
        FileNotFoundError: If the source image doesn't exist.
    """
    src = Path(image_path)
    if not src.is_file():
        raise FileNotFoundError(f"Image not found: {src}")

    orig_img = cv2.imread(str(src))
    if orig_img is None:
        raise ValueError(f"Could not read image: {src}")

    orig_h, orig_w = orig_img.shape[:2]
    resized = cv2.resize(orig_img, (width, height), interpolation=cv2.INTER_AREA)

    print(f"  ✅ Resized: ({orig_w}x{orig_h}) → ({width}x{height})")

    if output_path:
        cv2.imwrite(str(output_path), resized)
        print(f"  Saved to: {output_path}")

    cv2.imshow("Original", orig_img)
    cv2.imshow("Resized", resized)

    print("  Press 'q' to close windows.")
    if cv2.waitKey(0) & 0xFF == ord("q"):
        cv2.destroyAllWindows()


if __name__ == "__main__":
    print("── Image Resizing ──")
    try:
        resize_image("laptops.jpg", width=400, height=250)
    except FileNotFoundError as e:
        print(f"  ⚠️ {e}")

# For more on Python follow: https://x.com/rs_punia_
