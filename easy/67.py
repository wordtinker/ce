"""
You will be given a hexadecimal (base 16) number. Convert it into decimal
(base 10).
Input sample:
Your program should accept as its first argument a path to a filename. Each
line in this file contains a hex number. You may assume that the hex number does
not have the leading 'Ox'. Also all alpha characters (a through f) in the input
will be in lowercase. E.g.
9f
11

Output sample:
Print out the equivalent decimal number. E.g.

159
17
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        print(int(line, 16))