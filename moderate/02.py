"""
LONGEST LINES
CHALLENGE DESCRIPTION:


Write a program which reads a file and prints to stdout the specified number of the longest lines that are sorted based on their length in descending order.

INPUT SAMPLE:

Your program should accept a path to a file as its first argument. The file contains multiple lines. The first line indicates the number of lines you should output, the other lines are of different length and are presented randomly. You may assume that the input file is formatted correctly and the number in the first line is a valid positive integer.

For example:

2
Hello World
CodeEval
Quick Fox
A
San Francisco
OUTPUT SAMPLE:

Print out the longest lines limited by specified number and sorted by their length in descending order.

For example:

San Francisco
Hello World

"""

import sys


def print_function(lines, num):
    """
    Print the num times the longest strings
    """
    for key in sorted(lines.keys(), reverse=True):
        for line in lines[key]:
            if num == 0:
                return

            print(line)
            num -= 1


with open(sys.argv[1], 'r') as test_cases:
    num = int(next(test_cases))
    length = 0
    lines = {}  # Dictinary {length_of_line:[line, line]}
    for line in test_cases:
        len_line = len(line)
        if len_line not in lines:
            lines[len_line] = []
        lines[len_line].append(line)

    print_function(lines, num)
