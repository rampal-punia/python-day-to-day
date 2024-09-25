import sys

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
print(next(gen))        # StopIteration iteration

'''
This `StopIteration` error suggest that we consume a generator. 
Means generator produces the values only once in the program life cycle.
''' 


