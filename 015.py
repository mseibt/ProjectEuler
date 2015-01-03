"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

from __future__ import division
from functools import reduce
from operator import mul


# Some combinatorics:
# illustrate the problem as a word of length 40
# it contains only two different characters,
# each of them represented 20 times
# there are (20+20)! / 20!*20! possibilities
print((2**10 * reduce(mul, range(21, 40, 2)) // reduce(mul, range(1, 11))))