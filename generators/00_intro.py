import sys

def generate_large_dataset(n):
    for i in range(n):
        yield i ** 2

# Using a generator
gen = generate_large_dataset(1000000)
print(f"Generator size: {sys.getsizeof(gen)} bytes")

# Using a list comprehension
list_comp = [i ** 2 for i in range(1000000)]
print(f"List comprehension size: {sys.getsizeof(list_comp)} bytes")

# Processing the generator in chunks
chunk_size = 1000
for _ in range(5):  # Process first 5 chunks
    chunk = [next(gen) for _ in range(chunk_size)]
    print(f"Processed chunk: {chunk[:5]}...")  # Show first 5 elements of each chunk