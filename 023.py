"""
Project Euler Problem 23
========================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

from __future__ import division
import math


# new limit with http://mathworld.wolfram.com/AbundantNumber.html
limit = 20161
abundants = []
for i in range(2, limit+1):
    s = 1
    # Could be written in a listcomprehension
    # however, it would require additional memory
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            s += j + i//j
    if int(math.sqrt(i)) == math.sqrt(i):
        s -= int(math.sqrt(i))
    if s > i:
        abundants.append(i)

abundants = set(abundants)
print(sum(i for i in range(limit+1) if not any(i-a in abundants for a in abundants)))