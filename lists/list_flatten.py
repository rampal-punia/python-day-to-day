'''✨ Python: Flatten a Nested List ✨'''

nested = [[1, 2], [3, 4], [5, 6]]
# Required Output: [1, 2, 3, 4, 5, 6]

flat = [i for sublist in nested for i in sublist]
print(flat)


# For more on Python follow: https://x.com/rs_punia_
