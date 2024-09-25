'''✨ Python: Convert a Color Image To Grayscale using OpenCV ✨'''

import cv2

# Read orig image
orig_img = cv2.imread('operations_on_images/laptops.jpg')

# Show orig image
cv2.imshow('Orig Image', orig_img)

# Code to convert orig image to Gray scale
gray_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)

# Show Gray scale image
cv2.imshow('Gray scale Image', gray_img)


if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
print("done")


# For more on Python follow: https://x.com/rs_punia_
