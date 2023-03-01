'''✨ Python Quiz: Using round() function ✨ 

What is the result of the following code snippet?
A) True
B) False
C) Erorr
'''

statement_1 = round(1.5 + True)
statement_2 = round(1.5 + False)

print(statement_1 == statement_2)

# Output: ??? 💭


######################################################################
# Answer:- A True

# Explanation:
''' We need to understand 2 things here.

1. How round() function works!
2. True and False are the subset of Python Data type int

Python 3 uses 'round half to even'. This means if we pass 5 after the 
point(any_integer.5) it will round it to an even number. But if we try 
`print(round(5.3))`. We will get 5 which is an odd number.

bool True has value 1 and False has value 0 as both are the subset of int.

Therefore (2 == 2) ==> True.

Thus, Answer B is solution
'''


# For more on Python follow: https://twitter.com/CodingMantras
