"""
Capitalize the words.
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        new_line = ' '.join((word[0].upper() + word[1:] for word in line.split()))
        print(new_line)