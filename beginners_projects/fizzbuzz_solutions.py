'''✨ # 3 Different ways to solve FIZZBUZZ problem in Python ✨'''

# First let us see what is a FIZZBUZZ problem in Programming?

'''
FIZZBUZZ Problem:
    For a given number 'n', output:

    Fizz - If the number is divisible by 3
    Buzz - If the number is divisible by 5
    FizzBuzz - if the number is divisible by both 3 and 5
    Number itself - if the number cannot be divided by 3 or 5.
'''


def fizzbuzz(n):
    # 📋 Method-1: Using normal function and if-else conditions
    for number in range(1, n):
        if (number % 3 == 0) and (number % 5 == 0):
            print("FizzBuzz", end=' ')
        elif (number % 3 == 0):
            print("Fizz", end=' ')
        elif (number % 5 == 0):
            print("Buzz", end=' ')
        else:
            print(number, end=' ')
    return


print(fizzbuzz(101))

# 📋 Using Lambda Function

'''
fizzbuzz = lambda n: "FizzBuzz" if n % 15 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else str(n)

print([fizzbuzz(i) for i in range(1, 101)])

'''
# 📋 Using List-Comprehension
print(['FizzBuzz' if i % 15 == 0 else 'Fizz' if i %
       3 == 0 else 'Buzz' if i % 5 == 0 else i for i in range(1, 101)])


# For more on Python follow: https://twitter.com/CodingMantras
