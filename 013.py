"""
Project Euler Problem 13
========================

Work out the first ten digits of the sum of the following one-hundred
50-digit numbers.


[Text: 013_numbers.txt]
"""

# trivial in python
print(str(sum([int(l) for l in open('resources/013_numbers.txt')]))[:10])