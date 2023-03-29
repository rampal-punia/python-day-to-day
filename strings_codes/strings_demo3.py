'''✨ Get substring

Different way to get 'is' from my_string = "Life is Awesome!!!"
✨'''
import re

my_string = "Python is Awesome!!!"

# Method 1: Using Index() method of string
index_of_is = my_string.index("is")
substring = my_string[index_of_is:index_of_is + 2]
print(substring)

# Method 2: Using String slicing
substring = my_string[5:7]
print(substring)

# Method 3: Using regular expression
substring = re.search("is", my_string).group()
print(substring)

# Method 4: Using split() method
split_list = my_string.split(" ")
substring = split_list[1]
print(substring)

# Method 5: Using partition() method of string
partition_tuple = my_string.partition("is")
substring = partition_tuple[1]
print(substring)

# Method 6: Using strings formatting
my_string = "Life is Awesome!!!"
substring = "{} {}".format(my_string[5], my_string[6])
print(substring)


# For more on Python follow: https://twitter.com/CodingMantras
