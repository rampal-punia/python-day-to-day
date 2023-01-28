# For more on Python follow: https://twitter.com/CodingMantras


'''✨ The comma is not an operator in Python, but a 
separator between expressions. ✨
'''
# Question
expression = "a" in "b", "a"

# What would be the output of this print statement
print(expression)

# Ans: (False, 'a')

# Reason: As described above:
# "The comma is not an operator in Python, but a
# separator between expressions."

# Therefore:
# ✅ Correct:
expression = ("a" in "b"), "a"

# ❌ Incorrect:
expression = "a" in ("b", "a")
