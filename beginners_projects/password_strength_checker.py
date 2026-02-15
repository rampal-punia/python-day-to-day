"""
Password Strength Checker & Generator
=======================================
Analyze password strength and generate secure passwords.

Author: @rampal-punia
"""

import string
import secrets
import re
from collections import Counter


def check_password_strength(password: str) -> dict:
    """
    Evaluate password strength based on multiple criteria.
    Returns a dict with score, rating, and detailed feedback.
    """
    score = 0
    feedback = []
    checks = {}

    # Length check
    length = len(password)
    checks["length"] = length
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("❌ Use at least 8 characters (12+ recommended)")

    # Character variety
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    checks["uppercase"] = has_upper
    checks["lowercase"] = has_lower
    checks["digits"] = has_digit
    checks["special_chars"] = has_special

    if has_upper:
        score += 1
    else:
        feedback.append("❌ Add uppercase letters")

    if has_lower:
        score += 1
    else:
        feedback.append("❌ Add lowercase letters")

    if has_digit:
        score += 1
    else:
        feedback.append("❌ Add digits")

    if has_special:
        score += 2
    else:
        feedback.append("❌ Add special characters (!@#$%...)")

    # Common patterns check
    common_patterns = [
        r"(.)\1{2,}",          # repeated characters (aaa)
        r"(012|123|234|345|456|567|678|789)",  # sequential numbers
        r"(abc|bcd|cde|def|efg)",  # sequential letters
        r"(?i)(password|qwerty|letmein|admin|welcome)",  # common words
    ]

    for pattern in common_patterns:
        if re.search(pattern, password):
            score -= 1
            feedback.append("⚠️  Contains common/predictable pattern")
            break

    # Entropy check (character diversity)
    char_freq = Counter(password)
    unique_ratio = len(char_freq) / max(length, 1)
    if unique_ratio > 0.7:
        score += 1

    # Final rating
    score = max(0, min(score, 10))  # clamp 0-10

    if score >= 8:
        rating = "🟢 STRONG"
    elif score >= 5:
        rating = "🟡 MODERATE"
    elif score >= 3:
        rating = "🟠 WEAK"
    else:
        rating = "🔴 VERY WEAK"

    if not feedback:
        feedback.append("✅ Password meets all criteria!")

    return {
        "password": password,
        "score": f"{score}/10",
        "rating": rating,
        "length": length,
        "checks": checks,
        "feedback": feedback,
    }


def generate_password(
    length: int = 16,
    uppercase: bool = True,
    lowercase: bool = True,
    digits: bool = True,
    special: bool = True,
    exclude_ambiguous: bool = True,
) -> str:
    """
    Generate a cryptographically secure random password.
    Uses `secrets` module (not `random`!) for security.
    """
    chars = ""
    required = []

    if uppercase:
        pool = string.ascii_uppercase
        if exclude_ambiguous:
            pool = pool.replace("O", "").replace("I", "")
        chars += pool
        required.append(secrets.choice(pool))

    if lowercase:
        pool = string.ascii_lowercase
        if exclude_ambiguous:
            pool = pool.replace("l", "").replace("o", "")
        chars += pool
        required.append(secrets.choice(pool))

    if digits:
        pool = string.digits
        if exclude_ambiguous:
            pool = pool.replace("0", "").replace("1", "")
        chars += pool
        required.append(secrets.choice(pool))

    if special:
        pool = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        chars += pool
        required.append(secrets.choice(pool))

    if not chars:
        raise ValueError("At least one character type must be enabled")

    # Fill remaining length with random chars
    remaining = length - len(required)
    password_chars = required + [secrets.choice(chars) for _ in range(remaining)]

    # Shuffle to avoid predictable positions
    password_list = list(password_chars)
    # Fisher-Yates shuffle using secrets
    for i in range(len(password_list) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_list[i], password_list[j] = password_list[j], password_list[i]

    return "".join(password_list)


def generate_passphrase(word_count: int = 4, separator: str = "-") -> str:
    """Generate a memorable passphrase from common words."""
    words = [
        "tiger", "mountain", "crystal", "thunder", "garden", "sunset",
        "diamond", "falcon", "harbor", "silver", "dragon", "breeze",
        "cobalt", "ember", "forest", "golden", "hollow", "ivory",
        "jasper", "knight", "lantern", "marble", "nebula", "orchid",
        "phoenix", "quartz", "ripple", "summit", "tornado", "velvet",
    ]
    chosen = [secrets.choice(words).capitalize() for _ in range(word_count)]
    # Add a random number for extra entropy
    chosen.append(str(secrets.randbelow(100)))
    return separator.join(chosen)


# ─────────────────────────────────────────────────
# DEMO
# ─────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("🔐 Password Strength Checker")
    print("=" * 55)

    test_passwords = [
        "password",
        "MyP@ss123",
        "correct-horse-battery-staple",
        "Kj#9xQ!mP2@nL7vR",
    ]

    for pwd in test_passwords:
        result = check_password_strength(pwd)
        print(f"\n  Password: {result['password']}")
        print(f"  Rating  : {result['rating']} ({result['score']})")
        for fb in result["feedback"]:
            print(f"  {fb}")

    print("\n" + "=" * 55)
    print("🔑 Password Generator")
    print("=" * 55)

    for length in [12, 16, 20]:
        pwd = generate_password(length=length)
        strength = check_password_strength(pwd)
        print(f"\n  Length {length}: {pwd}")
        print(f"  Rating  : {strength['rating']}")

    print("\n" + "=" * 55)
    print("📝 Passphrase Generator")
    print("=" * 55)

    for _ in range(3):
        phrase = generate_passphrase()
        print(f"  {phrase}")
