"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from __future__ import division


# Beautiful pythonic solution. The range() function builds a list like
# [3, 6, 9, ... 999] and [5, 10, 15, ..., 995]. The set() function returns
# distinct values, so multiples of 15 do not get added up twice.
def e001a():
    return sum(set(list(range(3, 1000, 3)) + list(range(5, 1000, 5))))


# Naive solution - build a list using a listcomprehension. Running through
# the full loop and check if a number is divisble by 3 or 5. Eventually build
#  the sum() over all listelements:
def e001b():
    return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])


# A modified version of the sumformula:
# Sum_{k=1}^{n}(k) = n * (n + 1) / 2
# 3 + 6 + 9 + 12 + ... + 999 = 3 * (1 + 2 + 3 + 4 + ...)
# 3 + 6 + 9 + 12 + ... + 999 = 3 * Sum_{k=1}^{floor(999/3)} =
# = 3 * (999/3) * (999/3 + 1) / 2
# same for 5 + 10 + 15 + ... + 995 = 5 * (999/5) * (999/5 + 1) / 2
# now we took k*3*5 two times,
# so we have to take these numbers into account too:
# 15 + 30 + ... + 990 =  15 * (999/15) * (999/15 + 1) / 2
def e001c():
    return (3*(999//3)*(999//3+1) + 5*(999//5)*(999//5+1)
            - 15*(999//15)*(999//15+1)) // 2


# builds the same expression as in e001c using lambda and the mapfunction
def e001d():
    return sum(map(lambda x: x*(999//x)*(999//x+1), [3, 5, -15])) // 2


print(e001a())