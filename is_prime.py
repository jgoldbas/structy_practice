"""
Determine if a number is prime. Return True if it is.
"""
from math import sqrt, floor
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True

print(is_prime(7))
print(is_prime(4))