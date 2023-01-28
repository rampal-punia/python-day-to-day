'''✨ Resize an Image. ✨'''

import cv2

# Read orig image
orig_img = cv2.imread('operations_on_images/laptops.jpg')

# Resize orig image to fit screen
resized = cv2.resize(orig_img, (400, 250))

# Show orig image
cv2.imshow('Orig Image', orig_img)

# Show resized image
cv2.imshow('Resized Image', resized)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
print("done")


# For more on Python follow: https://twitter.com/CodingMantras
