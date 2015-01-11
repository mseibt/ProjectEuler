"""
Often used methods for Project Euler Problems
"""

from __future__ import division
import math

# The often used function operator.mul
# within reduce can be rewritten using
# the lambda function: lambda x, y: x*y


def sum_digits(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


def faculty_list(length):
    f = [1, 1]
    if length == 0:
        return []
    if length == 1:
        return [1]
    if length == 2:
        return f
    for i in range(2, length):
        f.append(f[i-1]*i)
    return f


def fibonacci_limit(limit):
    a, b = 1, 2
    while a < limit:
        yield a
        a, b = b, a+b


def fibonacci_element(x):
    a, b = 1, 2
    for i in range(x):
        yield a
        a, b = b, a+b


def fibonacci_n(x):
    return round((((1 + 5**0.5) / 2)**x - (1 - ((1 + 5**0.5) / 2))**x) / 5**0.5)


def generate_circulars(number):
    length = math.ceil(math.log10(number))
    circulars = []
    for i in range(length-1):
        mod = number % 10
        number //= 10
        number += mod*10**(length-1)
        circulars.append(number)
    return circulars


def palindromic_number(n, base=10):
    return reverse_number(n, base) == n


def palindromic_string(s):
    return s == s[::-1]


def prime_sieve(n):
    n += 1
    sieve = [False for i in range(n+1)]
    sqrt = int(math.ceil(math.sqrt(n)))
    sieve[0] = True
    sieve[1] = True
    for i in range(2, sqrt+1, 1):
        if not sieve[i]:
            for j in range(n//i, i-1, -1):
                if not sieve[j]:
                    sieve[i*j] = True
    return sieve


def prime_numbers(limit):
    return [i for i, n in enumerate(prime_sieve(limit)) if n is False]


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    # n  is definitely composite
    return True


# From http://rosettacode.org/wiki/Miller-Rabin_primality_test#Python
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


def reverse_number(n, base=10):
    rev = 0
    while n > 0:
        rev = base*rev + n % base
        n //= base
    return rev