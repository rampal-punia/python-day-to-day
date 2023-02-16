x = {9, 8, 5}
y = {9, 5, 8}
print(x == y)       # <-- True
print(x is y)       # <-- False
print(id(x))        # 140132936219552
print(id(y))        # 140132937292704

x = [9, 8, 5]
y = [9, 5, 8]
print(x == y)       # <-- False
print(x is y)       # <-- False

x = (9, 8, 5)
y = (9, 5, 8)
print(x == y)       # <-- False
print(x is y)       # <-- False
