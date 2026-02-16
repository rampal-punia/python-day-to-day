"""Color to Grayscale — Convert a color image to grayscale using OpenCV.

Difficulty: 🟢 Easy
Topics: OpenCV, cv2.cvtColor, COLOR_BGR2GRAY, image I/O
Requires: pip install opencv-python

Author: @rampal-punia
"""

from pathlib import Path
import cv2


def convert_to_grayscale(
    image_path: str | Path, output_path: str | Path | None = None
) -> None:
    """Convert a color image to grayscale and display both.

    Args:
        image_path: Path to the source color image.
        output_path: Optional path to save the grayscale image.

    Raises:
        FileNotFoundError: If the source image doesn't exist.
    """
    src = Path(image_path)
    if not src.is_file():
        raise FileNotFoundError(f"Image not found: {src}")

    orig_img = cv2.imread(str(src))
    if orig_img is None:
        raise ValueError(f"Could not read image: {src}")

    gray_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)

    if output_path:
        cv2.imwrite(str(output_path), gray_img)
        print(f"  ✅ Saved grayscale image: {output_path}")

    cv2.imshow("Original", orig_img)
    cv2.imshow("Grayscale", gray_img)

    print("  Press 'q' to close windows.")
    if cv2.waitKey(0) & 0xFF == ord("q"):
        cv2.destroyAllWindows()


if __name__ == "__main__":
    print("── Color to Grayscale Conversion ──")
    try:
        convert_to_grayscale("laptops.jpg", "laptops_gray.jpg")
    except FileNotFoundError as e:
        print(f"  ⚠️ {e}")

# For more on Python follow: https://x.com/rs_punia_
