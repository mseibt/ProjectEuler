"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from __future__ import division


n = 1000000

# Using a hashtable to make the algorithm faster
# if we reach a previously calculated number just add
# the amount of steps.
table = [0 for i in range(n+1)]
for i in range(2, n+1):
    tmp = i
    steps = 0
    while tmp != 1:
        # Collatz sequencing
        tmp = tmp//2 if tmp % 2 == 0 else 3*tmp + 1
        steps += 1
        if tmp < len(table):
            if table[tmp] != 0:
                steps += table[tmp]
                tmp = 1
    table[i] = steps

print(table.index(max(table)))