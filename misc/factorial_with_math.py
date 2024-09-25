'''✨ Different ways to find Factorial of a given number. ✨'''
import numpy as np
from functools import reduce
import math

x = 20
# Method 1: Using factorial function from math module
factorial = math.factorial(x)
print(factorial)

# Method 2: Using prod function from math module
factorial = math.prod(list(range(1, x+1)))
print(factorial)


# Method 3: Using reduce function from functools module
factorial = reduce(lambda result, num: result*num, range(1, x+1), 1)
print(factorial)


# Method 4: Using prod function from numpy module
factorial = np.prod(list(range(1, x+1)))
print(factorial)


# For more on Python follow: https://x.com/rs_punia_
