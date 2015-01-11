"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from __future__ import division

from Euler import prime_numbers


# Very slow :( -> 52seconds
# i guess the right way is to somehow "generate" these numbers
primes = prime_numbers(1000000)
s = 0
count = 0
# exclude 2, 3, 5, 7
for prime in primes[4:]:
    is_truncatable = True
    # truncate right to left
    tmp = prime
    while tmp > 0:
        tmp //= 10
        if tmp not in primes and tmp != 0:
            is_truncatable = False
            break

    if is_truncatable:
        # truncate left to right
        tmp = prime
        modulus = 10
        while tmp % modulus != tmp:
            if tmp % modulus not in primes:
                is_truncatable = False
                break
            modulus *= 10

    if is_truncatable:
        s += prime
        count += 1
        if count == 11:
            break

print(s)