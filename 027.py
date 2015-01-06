"""
Project Euler Problem 27
========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""

from Euler import prime_sieve

sieve = prime_sieve(1000000)
max_primes = 0
product = 0

for a in range(-999, 1000, 1):
    for b in range(-999, 1000):
        primes = 0
        prime = True
        while prime:
            n = primes * primes + a * primes + b
            if n > 0:
                if not sieve[n]:
                    primes += 1
                else:
                    prime = False
            else:
                prime = False
        if max_primes < primes:
            max_primes = primes
            product = a*b

print(product)