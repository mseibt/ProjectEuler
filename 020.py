"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""

from functools import reduce
from operator import mul

from Euler import sum_digits


print(sum_digits(reduce(mul, range(1, 101))))