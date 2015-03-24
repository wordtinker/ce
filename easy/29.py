"""
UNIQUE ELEMENTS
CHALLENGE DESCRIPTION:


You are given a sorted list of numbers with duplicates. Print out the sorted list with duplicates removed.

INPUT SAMPLE:

File containing a list of sorted integers, comma delimited, one per line. E.g.

1,1,1,2,2,3,3,4,4
2,3,4,5,5
OUTPUT SAMPLE:

Print out the sorted list with duplicates removed, one per line.
E.g.

1,2,3,4
2,3,4,5

"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        s_list = line.split(',')
        i_set = sorted(set(int(i) for i in s_list))
        s_set = (str(i) for i in i_set)
        print(','.join(s_set))