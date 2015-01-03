"""
Project Euler Problem 11
========================

In the 20 * 20 grid below, four numbers along a diagonal line have been
marked in red.


[Text: 011_numbers.txt]

The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

What is the greatest product of four adjacent numbers in any direction
(up, down, left, right, or diagonally) in the 20 * 20 grid?
"""

from functools import reduce
from operator import mul


n = [list(map(int, l.split())) for l in open('resources/011_numbers.txt')]
maximum = 0


# Custom access to the numbers so we don't have to care about borders
def get_grid(x, y):
    return n[x][y] if 0 <= x < 20 and 0 <= y < 20 else 0

# Simple brute force
for i in range(20):
    for j in range(20):
        maximum = max(
            maximum,
            reduce(mul, [get_grid(i+n, j) for n in range(4)]),
            reduce(mul, [get_grid(i+n, j+n) for n in range(4)]),
            reduce(mul, [get_grid(i, j+n) for n in range(4)]),
            reduce(mul, [get_grid(i-n, j+n) for n in range(4)])
        )

print(maximum)