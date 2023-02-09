'''✨ Python: Flatten a Nested Dictionary ✨'''

import itertools

nested_dict = {1: {2: 3}, 4: {5: 6}}
# Required output only dictionaries: {2: 3, 5: 6}


# Method 1:
flattened_dict = {k: v for d in nested_dict.values() for k, v in d.items()}
print(flattened_dict)

# Method 2:
flattened_dict = dict(itertools.chain.from_iterable(
    [d.items() for d in nested_dict.values()]))
print(flattened_dict)


# For more on Python follow: https://twitter.com/CodingMantras
