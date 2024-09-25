'''✨ Python Quiz ✨ 

What would be the output:
A) 0
B) TypeError
C) SyntaxError
D) 1
'''
import builtins
max = 100
numbers = list(range(10))
print(max(numbers))
# Output: ??? 💭


# Answer:-
# However we can use this code as a work-around to this issue.

max = 0
my_list = list(range(10))
max_of_list = builtins.max(my_list)
print(max_of_list)


# For more on Python follow: https://x.com/rs_punia_
