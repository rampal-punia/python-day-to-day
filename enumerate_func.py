'''✨ Python: Using Enumerate 

Enumerate is a built-in function in Python used to add counter
to an iterable and returns it in a form of enumerate object. 
The object returned by enumerate is an iterator containing 
pairs (index, element), where index starts from 0 by default. 
Here's an example:

✨'''

colors = ['Red', 'Black', 'Orange', 'Yellow', 'Green']

for index, color in enumerate(colors):
    print(f"{index=}, {color=}")

# specify the starting index as the second argument to enumerate
for index, color in enumerate(colors, start=1001):
    print(f"{index=}, {color=}")


# For more on Python follow: https://twitter.com/CodingMantras
