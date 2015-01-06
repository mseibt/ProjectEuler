"""
Project Euler Problem 24
========================

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?
"""

from __future__ import division


faculty = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

permcount = 999999
result = 0

# we have 1M permutations. 362880 (9!)  are starting with 0
# 362880 are starting with 1 etc
# 3*362880 > 1M thus the first char must be 2
# 1M-2*362880 = 274240
# now we do the same with 274240 and 8! and go on until 0!
for i in range(9, 0, -1):
    tmp = permcount // faculty[i]
    permcount %= faculty[i]
    result = result*10 + digits[tmp]
    while tmp <= i and tmp+1 < len(digits):
        digits[tmp] = digits[tmp+1]
        tmp += 1

print(result*10+digits[0])