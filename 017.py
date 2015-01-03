"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

# len("one") = len("and") = 3
# len("onetwothree...nine") = 36
# len("teneleven...nineteen") = 70
# len("twenty...ninety") = 46
# len("hundred") = 7
# len("thousand") = 8 */
print(
    11 +        # one thousand
    900 * 7 +   # hundred
    190 * 36 +  # onetwothree...nine
    10 * 70 +   # teneleven...nineteen
    100 * 46 +  # twentythirty...ninety
    891 * 3     # and
)