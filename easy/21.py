"""
SUM OF DIGITS
CHALLENGE DESCRIPTION:

Given a positive integer, find the sum of its constituent digits.

INPUT SAMPLE:

The first argument will be a path to a filename containing positive integers, one per line. E.g.

23
496
OUTPUT SAMPLE:

Print to stdout, the sum of the numbers that make up the integer, one per line. E.g.

5
19
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        s = 0
        for char in line.strip():
            s += int(char)
        print(s)