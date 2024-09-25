'''✨ Python: Yield vs append in List ✨'''

nums = range(1000)


def yielding():
    def yielder():
        for n in nums:
            yield n
    return list(yielder())


def appending():
    lst = []
    for n in nums:
        lst.append(n)
    return lst


print(yielding())
print("yielding exhausted ")
print(yielding())
# For more on Python follow: https://x.com/rs_punia_
