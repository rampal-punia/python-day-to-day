# Adding Numbers
num1 = 1
num2 = 2
print(num1 + num2)  # Output: 3

# Adding strings
str1 = "Hello"
str2 = "world"
print(str1 + " " + str2)  # Output: "Hello world"

# Adding numbers as string-literals
str_num1 = "5"
str_num2 = "2"
print(str_num1 + str_num2)  # Output: 52

# Adding lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # Output: [1, 2, 3, 4, 5, 6]

# Adding tuples:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)  # Output: (1, 2, 3, 4, 5, 6)

# Adding sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 + set2)
# Raises a TypeError:
# unsupported operand type(s) for +: 'set' and 'set'

# Adding floats
float1 = 1.5
float2 = 2.5
print(float1 + float2)  # Output: 4.0
