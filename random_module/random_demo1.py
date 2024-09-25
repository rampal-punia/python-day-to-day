'''✨ Generate random RGB color values.✨'''
import random

# Method 1:
rgb_color = tuple(random.randint(0, 255) for _ in range(3))
print(rgb_color)

# Method 2:
rgb_color = tuple(random.sample(range(256), 3))
print(rgb_color)

# For more on Python follow: https://x.com/rs_punia_
