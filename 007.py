"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

from Euler import prime_sieve


primes = prime_sieve(1000000)
counter = 0
i = 1
# Simple search in the prime sieve
while counter < 10001:
    i += 1
    if not primes[i]:
        counter += 1

print(i)