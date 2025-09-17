"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

def is_factor(d, n):
    return n % d == 0
    pass

def is_prime(n):
    if n< 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if is_factor(i, n):
            return False
    return True
    pass

list_of_primes = [x for x in range(1, 10001) if is_prime(x)]
print(list_of_primes)