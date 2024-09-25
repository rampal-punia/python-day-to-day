'''✨ Python: Using Enumerate ✨

Enumerate is a built-in function in Python used to add counter
to an iterable and returns it in a form of enumerate object. 
The object returned by enumerate is an iterator containing 
pairs (index, element), where index starts from 0 by default. 
Here's an example:
'''

languages = ['Python', 'Rust', 'JavaScript']

# The default index will start from 0
for index, lang in enumerate(languages):
    print(f"{index=}, {lang=}")

# We can specify the starting index as the second argument to enumerate
for index, lang in enumerate(languages, start=1001):
    print(f"{index=}, {lang=}")


# For more on Python follow: https://x.com/rs_punia_
