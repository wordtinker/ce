"""
SUM OF INTEGERS FROM FILE
CHALLENGE DESCRIPTION:


Print out the sum of integers read from a file.

INPUT SAMPLE:

The first argument to the program will be a path to a filename containing a positive integer, one per line. E.g.

5
12
OUTPUT SAMPLE:

Print out the sum of all the integers read from the file. E.g.

17
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    summma = 0
    for test in test_cases:
        n = int(test)
        summma += n
    print(summma)