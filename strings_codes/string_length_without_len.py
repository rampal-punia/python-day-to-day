def string_length(string):
    length = 0
    for _ in string:
        length += 1
    return length


s = "Hello world!"
print(string_length(s))
print(len(s))
