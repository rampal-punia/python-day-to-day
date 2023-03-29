'''✨ Python Quiz: Yield Keyword ✨ 

What is the result of the following code snippet?
A) 1 4 9 16 25
B) 1 4 9 16
C) 1 4 9 16 25 36 49 64 81
D) Error, as no return statement inside function
'''


def square(start=1, stop=10):
    for n in range(start, stop):
        yield n * n


for i in square(start=1, stop=5):
    print(i, end=' ')

# Output: ??? 💭
