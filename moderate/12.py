"""
FIRST NON-REPEATED CHARACTER
CHALLENGE DESCRIPTION:


Write a program which finds the first non-repeated character in a string.

INPUT SAMPLE:

The first argument is a path to a file. The file contains strings.

For example:
yellow
tooth
OUTPUT SAMPLE:

Print to stdout the first non-repeated character, one per line.

For example:
y
h
SUBMIT SOLUTION
"""


import sys


def unique_letter(word):
    for i in range(len(word)):
        letter = word[i]
        if word.count(letter) == 1:
            return letter

with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        print(unique_letter(line.rstrip()))