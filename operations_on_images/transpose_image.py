'''✨ Python: Create Thumbnail of an image using Pillow. ✨'''

from PIL import Image

image = Image.open("laptops.jpg")

# Rotate image by 90 degrees clockwise
image = image.transpose(Image.Transpose.ROTATE_90)
image.save("image_rotated_90.jpg")

# Rotate image by 180 degrees
image = image.transpose(Image.Transpose.ROTATE_180)
image.save("image_rotated_180.jpg")

# Rotate image by 270 degrees clockwise
image = image.transpose(Image.Transpose.ROTATE_270)
image.save("image_rotated_270.jpg")


# For more on Python follow: https://twitter.com/CodingMantras
