elements = [int, "", 1, str]
print([callable(obj) for obj in elements])
[True, False, False, True]

# Notice the brackets () after int and str
elements = [int(), "", 1, str()]
print([callable(obj) for obj in elements])
[False, False, False, False]
