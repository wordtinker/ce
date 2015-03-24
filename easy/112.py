"""
You are given a list of numbers which is supplemented with positions that have
to be swapped.
Your program should accept as its first argument a path to a filename.
Input example is the following
1 2 3 4 5 6 7 8 9 : 0-8
1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3

As you can see a colon separates numbers with positions.
Positions start with 0.
You have to process positions left to right. In the example above (2nd line)
first you process 0-1, then 1-3.
Output sample:
Print the lists in the following way.

9 2 3 4 5 6 7 8 1
2 4 3 1 5 6 7 8 9 10
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        l_part, r_part = line.split(':')
        some_list = l_part.split()
        for pair in r_part.split(','):
            a, b = pair.split('-')
            some_list[int(a)], some_list[int(b)] = some_list[int(b)], some_list[int(a)]
        print(' '.join(some_list))