"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from __future__ import division

from Euler import faculty_list


faculty = faculty_list(10)


# Range
# 9! = 362880, 7*9! = 2540160
# -> For higher numbers the sum of the factorial of their digits
# is always lower than the number itself
def e034a():
    s = 0
    for i in range(10, 2540161):
        if i == sum([faculty[int(c)] for c in str(i)]):
            s += i
    return s


def e034b():
    s = 0
    for i in range(10, 2540161):
        t = i
        ts = 0
        while t > 0:
            ts += faculty[t % 10]
            t //= 10
        if ts == i:
            s += ts
    return s

# actually compare timings of str() and
# usage of % and / for this problem
# e034a() -> 7.5s
# e034b() -> 3.9s
print(e034b())