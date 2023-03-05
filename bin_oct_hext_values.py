number = 72

# Method 1️⃣: Using built-in bin(), oct(), and hex() functions
print(f"Binary: {bin(number)}")
print(f"Octal: {oct(number)}")
print(f"Hexadecimal: {hex(number)}")

# Method 2️⃣: Using string formatting with, 'b', 'o', and 'x'
print(f"Binary: {number:b}")
print(f"Octal: {number:o}")
print(f"Hexadecimal: {number:x}")

# output:
# Binary: 0b10010000
# Octal: 0o110
# Hexadecimal: 0x48
