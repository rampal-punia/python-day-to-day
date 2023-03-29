'''✨ Python: Random Password Generator✨ '''

import secrets
import string


def generate_password(length):
    punctuation = "#$&@"
    # Combination of ASCII letters and digits for password
    characters = string.ascii_letters + string.digits + punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password


length = int(input("Enter the desired length of your password: "))
print("Your generated password is:", generate_password(length))
