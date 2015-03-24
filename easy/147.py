"""
LETTERCASE PERCENTAGE RATIO
CHALLENGE DESCRIPTION:

Your task is to write a program which determines (calculates) the percentage ratio of lowercase and uppercase letters.

INPUT SAMPLE:

Your program should accept a file as its first argument. Each line of input contains a string with uppercase and lowercase letters.

For example:
thisTHIS
AAbbCCDDEE
N
UkJ
OUTPUT SAMPLE:

For each line of input, print the percentage ratio of uppercase and lowercase letters rounded to the second digit after the point.

For example:
lowercase: 50.00 uppercase: 50.00
lowercase: 20.00 uppercase: 80.00
lowercase: 0.00 uppercase: 100.00
lowercase: 33.33 uppercase: 66.67
SUBMIT SOLUTION
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        line = line.strip()
        uppercase = 0
        length = len(line)
        for char in line:
            if char.isupper():
                uppercase += 1
        u_perc = uppercase / length * 100
        l_perc = (length - uppercase) / length * 100
        print("lowercase: {:.2f} uppercase: {:.2f}".format(l_perc, u_perc))



# import sys
#
# with open(sys.argv[1], 'r') as test_cases:
#     for line in test_cases:
#         line = line.strip()
#         length = len(line)
#         uppercase = sum([1 for char in line if char.isupper()])
#         u_perc = uppercase / length * 100
#         l_perc = 100 - u_perc
#         print("lowercase: {:.2f} uppercase: {:.2f}".format(l_perc, u_perc))
