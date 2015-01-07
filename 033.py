"""
Project Euler Problem 33
========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

from __future__ import division


# we search for:
# ax/bx = a/b, a < b
# xa/xb = a/b, a < b
# xa/bx = a/b, xa < bx
# ax/xb = a/b, ax < xb
# Lets save the fractions out of curiosity
fractions = []
for a in range(1, 10):
    for b in range(1, 10):
        if a/b < 1:
            for x in range(1, 10):
                if a/b == ((a*10)+x) / ((b*10)+x):
                    fractions.append([a*10+x, b*10+x])
                if a/b == ((x*10)+a) / ((x*10)+b):
                    fractions.append([x*10+a, x*10+b])
                if a/b == ((x*10)+a) / ((b*10)+x):
                    fractions.append([x*10+a, b*10+x])
                if a/b == ((a*10)+x) / ((x*10)+b):
                    fractions.append([a*10+x, x*10+b])

# print(fractions)
num = 1
den = 1
for a, b in fractions:
    num *= a
    den *= b
i = 2
while i <= num:
    while num % i == 0 and den % i == 0:
        num //= i
        den //= i
    i += 1

print(den)