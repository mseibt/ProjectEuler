"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

s = 1000


# simple brute force
def e009a():
    for a in range(1, 500):
        for b in range(a, 500):
            if a**2 + b**2 == (s-a-b)**2:
                return a*b*(s-a-b)

# TODO:
# Using parametrisation of triangles.
# Project Euler Overview for more information

print(e009a())