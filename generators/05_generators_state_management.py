def countdown(n):
    print("Countdown starting!")
    while n > 0:
        yield n
        n -= 1


# Create a generator object
count_gen = countdown(5)

print(next(count_gen))  # Output: 5
print(next(count_gen))  # Output: 4
print(next(count_gen))  # Output: 3

print("*" * 50)
print("Doing something else here...")
for i in range(65, 91):
    print(chr(i), end=' ')
print()
print("*" * 50)

print("Resume count down")
print(next(count_gen))  # Output: 2
print(next(count_gen))  # Output: 1

try:
    print(next(count_gen))
except StopIteration:
    print("Countdown finished!")
