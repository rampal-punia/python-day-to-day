'''✨ all() 🆚 any() ✨'''

# 📋 all(): Return True if bool(x) is True for all values x
# in the iterable. If the iterable is empty, return True.

# 👉 Take a list with one false value. Here zero(0) is false.
l1 = [2, 3, 4, 6, 0, 8]
print(all(l1))      # False

# 👉 One more example with a few falsy value. Here [], {} are falsy.
l2 = (True, True, [1], [], {})
print(all(l2))      # False

# 👉 if all the values are true. What makes '[[]]' a true?
l3 = [True, [1, 2, 3], [[]]]
print(all(l3))      # True
# check
print(bool([[]]))   # True

# But if the iterable is empty.
l4 = []
print(all(l4))      # True

# 📋 any(): Return True if bool(x) is True for any x in
# the iterable. If the iterable is empty, return False.

# 👉 Take a list with one false value. Here zero(0) is false.
l1 = [2, 3, 4, 6, 0, 8]
print(any(l1))      # True

# 👉 One more example with a few falsy value. Here [], {} are falsy.
l2 = (True, True, [1], [], {})
print(any(l2))      # True

# 👉 if all the values are true.
l3 = [True, [1, 2, 3], 'John']
print(any(l3))      # True

# But if the iterable is empty.
l4 = []
print(any(l4))      # False


# For more on Python follow: https://x.com/rs_punia_
