"""
Project Euler Problem 16
========================

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from Euler import sum_digits


# trivial in python
def e016a():
    return sum(map(int, str(2**1000)))


# If you don't like the str()
def e016b():
    return sum_digits(2**1000)

print(e016b())