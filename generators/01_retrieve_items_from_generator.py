n = 5

def generate_largelist(n):
    # Creating generator from a function
    for i in range(n):
        yield i

gen = generate_largelist(n)

# Retrive values using __next__ dundur method
print(gen.__next__())   # 0
print(gen.__next__())   # 1
print(gen.__next__())   # 2

# Retrive values using next() method
print(next(gen))        # 3
print(next(gen))        # 4
# print(next(gen))        # StopIteration iteration

'''
This `StopIteration` error suggest that we consume a generator. 
Means generator produces the values only once in the program life cycle.

We can handle this error as well
'''

def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()

# Using next() function
print("Using next() function:")
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

# Using __next__() method
print("\nUsing __next__() method:")
print(gen.__next__())  # Output: 3

# Handling StopIteration
try:
    print(next(gen))
except StopIteration:
    print("Generator exhausted!")

# Creating a new generator
gen = simple_generator()

# Using a for loop (which uses next() internally)
print("\nUsing a for loop:")
for value in gen:
    print(value)


