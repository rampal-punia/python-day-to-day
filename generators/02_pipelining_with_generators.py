def generate_numbers(n):
    for i in range(n):
        yield i

def square(numbers):
    for num in numbers:
        yield num ** 2

def add_two(numbers):
    for num in numbers:
        yield num + 2

n = 10

# Create a pipeline
pipeline = add_two(square(generate_numbers(n)))

print(list(pipeline))
# [2, 3, 6, 11, 18, 27, 38, 51, 66, 83]

# If we try to reuse the pipeline (it's exhausted)
print(list(pipeline))   # []

# We can recreate the pipeline to use it again
pipeline = add_two(square(generate_numbers(n)))
print(list(pipeline))
# [2, 3, 6, 11, 18, 27, 38, 51, 66, 83]