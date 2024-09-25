'''✨ Python: Create Thumbnail of an image using Pillow. ✨'''

from PIL import Image


def change_format(image_path, required_format):
    # Open image with pillow
    image = Image.open(image_path)

    # Save image with required image format
    image.save(f"other_format.{required_format}")

    print(
        f"Current format: {image.format}, Converted Format: {required_format}")


change_format("laptops.jpg", "png")


# For more on Python follow: https://x.com/rs_punia_
