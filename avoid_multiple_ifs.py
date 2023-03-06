'''✨ Python: Avoid Multiple if-else conditions by using 
dictionaries key-values ✨ '''

# WRONG: Dont'do this


def position(index):
    if index == 1:
        return str(index) + "st"
    elif index == 2:
        return str(index) + "nd"
    elif index == 3:
        return str(index) + "rd"
    elif index == 11:
        return str(index) + "th"
    elif index == 12:
        return str(index) + "th"
    else:
        return str(index) + "th"

# CORRECT: Do this


def position(index):
    suffix = {1: 'st', 2: 'nd', 3: 'rd'}
    if index % 100 in [11, 12]:
        return str(index) + 'th'
    return str(index) + suffix.get(index % 10, 'th')


print(21 % 100)
print(11 % 100)
print(position(21))


# For more on Python follow: https://twitter.com/CodingMantras
