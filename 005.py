"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""


# Just use the prime factorization of all the numbers from 1 to 20
# and multiply them
def e005a():
    return 2 ** 4 * 3 ** 2 * 5 * 7 * 11 * 13 * 17 * 19


# Brute Force solution. Since 2520 is divisible by all numbers from
# 1 to 10, the number we are searching for must be divisible by 2520
def e005b():
    i = 2520
    while True:
        if sum([i % j for j in range(1, 21)]) == 0:
            return i
        i += 2520

print(e005a())