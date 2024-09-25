'''✨ Find Prime between a given range ✨'''

start_range = 20000
end_range = 100000


primes = [x for x in range(start_range, end_range) if all(
    x % y != 0 for y in range(2, int(x ** 0.5) + 1))]

print(primes)


# For more on Python follow: https://x.com/rs_punia_
