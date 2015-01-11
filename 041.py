"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations

from Euler import is_prime


# 1+2+3+4+5+6+7+8 = 36 -> divisible by 3
# -> 8 and 9 pandigitals not possible since divisible by 3
# start with 7654321 and make permutations
# test for prime via sieve or is_prime function
numbers = [7, 6, 5, 4, 3, 2, 1]
n = 0
found = False
for perm in permutations(numbers):
    n = sum([perm[i]*10**(6-i) for i in range(7)])
    if is_prime(n):
        break

print(n)