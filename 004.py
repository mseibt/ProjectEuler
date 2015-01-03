"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# Generate all products of 3-digit-numbers and add the element to the list
# if it is a palindromic number. Eventually take the maximum of the list.
# If you don't like the str() use  x%10 and x/10 to get access to every digit
# Check Euler.py for more information. (sum_digits())
# For the optimization in the range generators read the Project Euler
# Overview for the Problem.
print(
    max([i*j for i in range(999, 100, -1) for j in range(990, 110, -11)
         if str(i*j) == str(i*j)[::-1]])
)