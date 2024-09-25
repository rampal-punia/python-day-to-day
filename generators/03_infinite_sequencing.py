def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()

# First 10 fibincci numbers are
print([next(fib_gen) for _ in range(10)])

print("\nFibonacci numbers between 100 and 1000:")
fib_gen = fibonacci_generator()
for fib in fib_gen:
    if fib > 1000:
        break
    if fib >= 100:
        print(fib, end=" ")
print()