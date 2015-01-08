"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from Euler import palindromic_number


# Generate all products of 3-digit-numbers and add the element to the list
# if it is a palindromic number. Eventually take the maximum of the list.
# The palindromic number is 6 digits long
# p = 100000x + 10000y + 1000z + 100z + 10y + x
# p = 11(9091x + 910y + 100z)
# thus either i or j must be divisible by 11
def e004a():
    return (
        max([i * j for i in range(999, 100, -1) for j in range(990, 110, -11)
             if palindromic_number(i * j)])
    )


# same with strings
def e004b():
    return (
        max([i * j for i in range(999, 100, -1) for j in range(990, 110, -11)
             if str(i * j) == str(i * j)[::-1]])
    )


# trying to maximize efficiency
def e004c():
    m = 0
    for i in range(1000, 1, -1):
        for j in range(i, 1, -1):
            if 0 != i % 11 and 0 != j % 11:
                continue
            if i * j < m:
                break

            # if palindromic_number(i*j):
            # m = max(i*j, m)
            # strings are faster here
            if str(i * j) == str(i * j)[::-1]:
                m = max(i * j, m)
    return m


print(e004c())