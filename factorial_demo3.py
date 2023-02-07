'''✨ Find Factorial of a given number n. 

Using reduce from functools module of Python
✨'''
from functools import reduce

x = 10

factorial = 1 if x == 0 else reduce(
    lambda result, num: result*num, range(1, x+1))
print(factorial)


# For more on Python follow: https://twitter.com/CodingMantras
