'''✨ Python: Create Thumbnail of an image using Pillow. ✨'''

from PIL import Image


def create_thumbnail(image_path, size=(128, 128)):
    # Open image with pillow
    image = Image.open(image_path)

    # use thumbnail method from Image module
    image.thumbnail(size)

    # Save thumbnail
    image.save(f"thumbnail_{size[0]}_{size[1]}.jpg")


create_thumbnail("laptops.jpg")


# For more on Python follow: https://twitter.com/CodingMantras
