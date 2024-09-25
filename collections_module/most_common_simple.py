# For more on Python follow: https://x.com/rs_punia_


'''✨ Python: Find Most Common Letter in a Sentence.'''

import collections

string_to_count = "I love learning Python a Lot"

counts = collections.Counter(string_to_count.lower())
print(f"{counts=}")

# Print most common 3 letters from the given string.
print(f"Most common 3 letters are: {counts.most_common(3)}")


# Sort the list alphabetically
sorted_list = {k: v for k, v in sorted(
    counts.items(), key=lambda item: item[0])}
print(f"{sorted_list=}")
