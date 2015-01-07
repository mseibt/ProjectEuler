"""
Often used methods for Project Euler Problems
"""

from __future__ import division
import math

# The often used module operator.mul
# can be rewritten as a lambda function:
# lambda x, y: x*y


def sum_digits(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


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