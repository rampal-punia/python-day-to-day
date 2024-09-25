'''✨ Python: Create Thumbnail of an image using Pillow. ✨'''

from PIL import Image, ImageOps

image = Image.open("laptops.jpg")

# Mirror image along the horizontal axis
image_mirrored = ImageOps.mirror(image)
image_mirrored.save("image_mirrored_horizontally.jpg")


# For more on Python follow: https://x.com/rs_punia_
