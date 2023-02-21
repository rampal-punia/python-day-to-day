'''✨ List comprehensions Examples ✨'''

# Squaring a list of numbers using list comprehension:
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]


# Filtering even numbers from a list using list comprehension:
numbers = [1, 2, 3, 4, 5]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)  # Output: [2, 4]

# Creating a dictionary from two lists using list comprehension:
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(dictionary)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Flattening a 2D list using list comprehension:
list_of_lists = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in list_of_lists for item in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]

# Creating a list of even numbers from 1 to 100 using list comprehension:
even_numbers = [n for n in range(1, 101) if n % 2 == 0]
print(even_numbers)
# Output: [2, 4, 6, ..., 100]


# Convert a list of strings to integers
str_list = ['1', '2', '3', '4', '5']
int_list = [int(num) for num in str_list]
print(int_list)
# Output: [1, 2, 3, 4, 5]

# Find common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = [num for num in list1 if num in list2]
print(common_elements)
# Output: [3, 4, 5]


# Remove duplicates from a list
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_list = [num for i, num in enumerate(
    list_with_duplicates) if num not in list_with_duplicates[:i]]
print(unique_list)
# Output: [1, 2, 3, 4, 5]


# Transpose a matrix
matrix = [[1, 2], [3, 4], [5, 6]]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)
# Output: [[1, 3, 5], [2, 4, 6]]

# Filter out non-numeric values from a list
mixed_list = [1, 'a', 2, 'b', 3, 'c']
numeric_list = [num for num in mixed_list if isinstance(
    num, int) or isinstance(num, float)]
print(numeric_list)
# Output: [1, 2, 3]


# Sort a list of dictionaries by a specific key
people = [{'name': 'Alice', 'age': 25}, {
    'name': 'Bob', 'age': 20}, {'name': 'Charlie', 'age': 30}]
sorted_people = sorted(people, key=lambda x: x['age'])
print(sorted_people)
# Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]


# For more on Python follow: https://twitter.com/CodingMantras
