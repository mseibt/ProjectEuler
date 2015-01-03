"""
Project Euler Problem 8
=======================

Find the greatest product of thirteen consecutive digits in the 1000-digit
number.

[Text: 008_number.txt]
"""

from string import whitespace
from functools import reduce
from operator import mul


# brute force
# build a list containing each digit of the number as an element
n = [int(x) for line in open('resources/008_number.txt')
     for x in line if x not in whitespace]
# build the multiplication of each sub list of length 13 and pick the maximum
print(max([reduce(mul, n[i:i+13]) for i in range(len(n)-13)]))