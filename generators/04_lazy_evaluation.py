import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

def prime_list(n):
    return [x for x in range(2, n) if is_prime(x)]

def prime_generator(n):
    for x in range(2, n):
        if is_prime(x):
            yield x

n = 100000

# Using a list
start = time.time()
primes_list = prime_list(n)
print(f"First 10 primes from list: {primes_list[:10]}")
print(f"Time taken (list): {time.time() - start:.2f} seconds")


# Using a generator
start = time.time() 
primes_gen = prime_generator(n)
print(f"First 10 primes from generator: {[next(primes_gen) for _ in range(10)]}")
print(f"Time taken (list): {time.time() - start:.2f} seconds")