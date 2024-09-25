'''✨ Check if a number is prime ✨'''


def is_prime(n):
    return n > 1 and all(
        n % i for i in range(2, int(n ** 0.5) + 1))


print(is_prime(2))   # True
print(is_prime(17))  # True
print(is_prime(22))  # False


# For more on Python follow: https://x.com/rs_punia_
