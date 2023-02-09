'''✨ Python: Create Thumbnail of an image using Pillow. ✨'''

from PIL import Image

image = Image.open("laptops.jpg")

# Rotate image by 45 degrees
angle = 45
image = image.rotate(angle, expand=True)
image.save("image_rotated_45.jpg")


# For more on Python follow: https://twitter.com/CodingMantras
