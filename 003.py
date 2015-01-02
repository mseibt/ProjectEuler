"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from Euler import prime_numbers


# Really fast runtime.
def e003a(x):
    i = 1
    while x > 1:
        i += 1
        while x % i == 0:
            x /= i
    return i


# Precalculate prime numbers so x doesn't get checked for
# divisibility by non-primes
# might be more efficient for bigger numbers
def e003b(x):
    primes = prime_numbers(10000)
    i = -1
    while x > 1:
        i += 1
        while x % primes[i] == 0:
            x /= primes[i]
    return primes[i]

print(e003a(600851475143))