# For more on Python follow: https://twitter.com/CodingMantras


'''✨ Python: Find Most Common Letter in a Sentence.'''

import collections

string_to_count = "I love learning Python a Lot"

counts = collections.Counter(string_to_count.lower())
print(f"{counts=}")

# Print most common 5 letters
print(counts.most_common(5))


# Sort the list for alphabets
sorted_list = {k: v for k, v in sorted(
    counts.items(), key=lambda item: item[0])}
print(sorted_list)
