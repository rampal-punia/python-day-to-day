"""User Login & Registration App — Secure authentication with hashing.

Difficulty: 🟡 Intermediate → 🔴 Advanced
Topics: hashlib (PBKDF2), secrets, file I/O, getpass, input validation

Security improvements over the original version:
    - Uses PBKDF2-HMAC-SHA256 with a random salt (not bare SHA-256)
    - Salt is stored alongside the hash for each user
    - Validates line format when reading user file

Author: @rampal-punia
"""

import hashlib
import os
import secrets
import string
from getpass import getpass

USER_DETAILS_FILEPATH = "users.txt"
PUNCTUATIONS = "@#$%&"
DEFAULT_PASSWORD_LENGTH = 12
HASH_ITERATIONS = 260_000  # OWASP recommended minimum for PBKDF2-SHA256


# ── Password Generation ─────────────────────────────────────────────


def generate_password(length: int = DEFAULT_PASSWORD_LENGTH) -> str:
    """Generate a cryptographically secure random password.

    Args:
        length: Desired password length (8-16).

    Returns:
        A random string with letters, digits, and selected punctuation.
    """
    characters = string.ascii_letters + string.digits + PUNCTUATIONS
    return "".join(secrets.choice(characters) for _ in range(length))


# ── Password Hashing (PBKDF2 with salt) ─────────────────────────────


def hash_password(password: str, salt: bytes | None = None) -> tuple[str, str]:
    """Hash a password using PBKDF2-HMAC-SHA256 with a random salt.

    Args:
        password: The plaintext password.
        salt: Optional salt bytes; generates new salt if None.

    Returns:
        Tuple of (hex_salt, hex_hash).
    """
    if salt is None:
        salt = os.urandom(16)
    pw_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, HASH_ITERATIONS
    )
    return salt.hex(), pw_hash.hex()


def verify_password(password: str, hex_salt: str, hex_hash: str) -> bool:
    """Verify a password against a stored salt and hash.

    Args:
        password: The plaintext password to check.
        hex_salt: The stored salt in hex.
        hex_hash: The stored hash in hex.

    Returns:
        True if the password matches.
    """
    salt = bytes.fromhex(hex_salt)
    _, computed_hash = hash_password(password, salt)
    return secrets.compare_digest(computed_hash, hex_hash)


# ── User Storage ─────────────────────────────────────────────────────


def save_user(username: str, hex_salt: str, hex_hash: str) -> None:
    """Append a new user record to the users file.

    Format: username:salt:hash (one per line).
    """
    with open(USER_DETAILS_FILEPATH, "a") as f:
        f.write(f"{username}:{hex_salt}:{hex_hash}\n")


def user_exists(username: str) -> bool:
    """Check if a username already exists in the users file.

    Args:
        username: The username to look up.

    Returns:
        True if the user is found.
    """
    try:
        with open(USER_DETAILS_FILEPATH, "r") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) >= 1 and parts[0] == username:
                    return True
    except FileNotFoundError:
        pass  # File will be created on first registration
    return False


def get_user_credentials(username: str) -> tuple[str, str] | None:
    """Retrieve the salt and hash for a given username.

    Args:
        username: The username to look up.

    Returns:
        Tuple of (hex_salt, hex_hash) or None if not found.
    """
    try:
        with open(USER_DETAILS_FILEPATH, "r") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) == 3 and parts[0] == username:
                    return parts[1], parts[2]
    except FileNotFoundError:
        pass
    return None


# ── Input Validation ─────────────────────────────────────────────────


def validate_password_length(raw_input: str) -> int:
    """Validate that the password length is an integer between 8 and 16.

    Args:
        raw_input: The user's input string.

    Returns:
        A valid password length, defaulting to DEFAULT_PASSWORD_LENGTH.
    """
    try:
        length = int(raw_input)
        if not 8 <= length <= 16:
            raise ValueError
        return length
    except ValueError:
        print(f"  ⚠️  Invalid length. Using default ({DEFAULT_PASSWORD_LENGTH}).")
        return DEFAULT_PASSWORD_LENGTH


# ── User Actions ─────────────────────────────────────────────────────


def register() -> None:
    """Register a new user with an auto-generated password."""
    username = input("  Enter username: ").strip()
    if not username:
        print("  ❌ Username cannot be empty.")
        return
    if user_exists(username):
        print(f"  ❌ User '{username}' already exists.")
        return

    length = validate_password_length(input("  Password length (8-16): "))
    password = generate_password(length)
    hex_salt, hex_hash = hash_password(password)
    save_user(username, hex_salt, hex_hash)

    print(f"  ✅ User '{username}' created successfully.")
    print(f"  🔑 Your password: {password}")
    print("  ⚠️  Save this password — it cannot be recovered!")


def login() -> None:
    """Authenticate an existing user."""
    username = input("  Enter username: ").strip()
    credentials = get_user_credentials(username)

    if credentials is None:
        print(f"  ❌ User '{username}' not found.")
        return

    password = getpass("  Password: ")
    hex_salt, hex_hash = credentials

    if verify_password(password, hex_salt, hex_hash):
        print(f"  ✅ Welcome back, {username}!")
    else:
        print("  ❌ Incorrect password.")


# ── Main Menu ────────────────────────────────────────────────────────


def main() -> None:
    """Run the login/register menu loop."""
    print("═" * 40)
    print("   🔐 User Login & Registration")
    print("═" * 40)

    while True:
        print("\n  1. Register")
        print("  2. Login")
        print("  3. Exit")
        choice = input("  Enter choice (1/2/3): ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("  Goodbye! 👋")
            break
        else:
            print("  ❌ Invalid choice.")


if __name__ == "__main__":
    main()
