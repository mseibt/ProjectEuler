"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from __future__ import division

from Euler import generate_circulars, prime_sieve


sieve = prime_sieve(1000000)
counter = 0
for i, b in enumerate(sieve):
    if not b:
        is_circular = True
        circulars = generate_circulars(i)
        for circular in circulars:
            if sieve[circular]:
                is_circular = False
                break
        if is_circular:
            # circular of 11 is 11, thus we have to take the
            # amount of distinct circulars
            counter += len(set(circulars + [i]))
            # mark the sieve so circular primes are not getting
            # checked multiple times
            for circular in circulars:
                sieve[circular] = True

print(counter)