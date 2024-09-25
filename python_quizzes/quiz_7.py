'''✨ Python Quiz ✨ 

What would be the output:
A) [1, 2, 3, 4]
B) [1, 2, 3, 4, 4]
C) None
D) [4]
'''

my_list = list(range(1, 4))
my_list.append(4)
print(my_list)


# Output: ??? 💭

######################################################################
# Answer:-
# Simple answer the append method, Append object to the end of the list.
# and returns None

# In depth answer: Internally, append creates a new list [4]
# and calls the __add__ method to concatenate it with my_list.
# The resulting list [1, 2, 3, 4] is stored in my_list.
# Since append doesn't need to return anything, it returns None.

# For more on Python follow: https://x.com/rs_punia_
