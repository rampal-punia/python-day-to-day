'''✨ Generate random Hexagonal color values.

For example: #F436DB
✨'''
import secrets
import random

# Method 1:


def random_hex_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return f"#{red:02X}{green:02X}{blue:02X}"


print(random_hex_color())

# Method 2:
hex_color = f"#{random.randint(0, 0xFFFFFF):06X}"
print(hex_color)

# Method 3:
hex_color = f"#{secrets.token_hex(3).upper()}"
print(hex_color)

# Method 4:
hex_color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
print(hex_color)

# Method 5:
hex_color = '#{:06X}'.format(random.randrange(16**6))
print(hex_color)

# For more on Python follow: https://x.com/rs_punia_
