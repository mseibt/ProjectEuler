"""
Project Euler Problem 18
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

[Text: 018_triangle.txt]

NOTE: As there are only 16384 routes, it is possible to solve this problem
   by trying every route. However, Problem 67, is the same challenge with
a triangle containing one-hundred rows; it cannot be solved by brute
force, and requires a clever method! ;o)
"""

triangle = [[int(number) for number in line.split()]
            for line in open("resources/018_triangle.txt")]


# instead of searching the way with the maximum sum
# just add up the higher elements from the bottom to the top
# this works since we don't have to know the exact route through the triangle
# which gives the maximum
def e018a():
    for row in range(len(triangle) - 1, 0, -1):
        for col in range(0, row):
            triangle[row - 1][col] += max(triangle[row][col], triangle[row][col + 1])
    return triangle[0][0]


# If you start from top to bottom you have to take the maximum of the last row
# Also accessing indices is a bit harder
def e018b():
    for row in range(len(triangle)-1):
        for col in range(len(triangle[row])):
            if col == 0:
                triangle[row+1][col] += triangle[row][col]
            if col == len(triangle[row])-1:
                triangle[row+1][col+1] += triangle[row][col]
            else:
                triangle[row+1][col+1] += max(triangle[row][col], triangle[row][col+1])
    return max(triangle[-1])

print(e018b())