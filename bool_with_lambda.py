'''✨ Python: Booleans(True, False) are the subset of integers.
Refer the PEP-285: https://peps.python.org/pep-0285/
 ✨'''

# what would be the output

print((lambda a, b: a * b)(5, 4) - True)
# The lambda function will multiply two numbers and give the output: 20 here.

# So, the answer will be 19

# Check this
print(issubclass(bool, int))

# As the boolean True=1 and False=0. The result will be 20-1=19


# For more on Python follow: https://twitter.com/CodingMantras
