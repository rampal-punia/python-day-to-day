'''✨ Find Prime between a given range of input from a user ✨'''

print("Enter two space-numbers below")

# Sample input = 1000 5000
start_range, end_range = list(map(int, input().split()))


primes = [x for x in range(start_range, end_range) if all(
    x % y != 0 for y in range(2, int(x ** 0.5) + 1))]

print(primes)


# For more on Python follow: https://twitter.com/CodingMantras
