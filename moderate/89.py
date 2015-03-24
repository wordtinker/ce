"""
PASS TRIANGLE
CHALLENGE DESCRIPTION:

By starting at the top of the triangle and moving to adjacent numbers on the row below, the maximum total from top to bottom is 27.

   5
  9 6
 4 6 8
0 7 1 5
5 + 9 + 6 + 7 = 27

INPUT SAMPLE:

Your program should accept as its first argument a path to a filename. Input example is the following:
5
9 6
4 6 8
0 7 1 5
You make also check full input file which will be used for your code evaluation.

OUTPUT SAMPLE:

The correct output is the maximum sum for the triangle. So for the given example the correct answer would be
27
"""


import sys


def blend(upper, lower):
    if upper:
        length = len(upper)
        for i, n in enumerate(upper):
            if i == 0:  # Leftmost number in line
                lower[0] += n

            if i == length - 1:  # Rightmost number in line
                lower[-1] += n
            else:  # Number in lower line can 'inherit' from two numbers
                lower[i + 1] += max(n, upper[i + 1])
    return lower


with open(sys.argv[1], 'r') as test_input:
    floating_sum = []
    for line in test_input:
        line = line.rstrip()
        line = [int(i) for i in line.split()]
        floating_sum = blend(floating_sum, line)

print(max(floating_sum))
