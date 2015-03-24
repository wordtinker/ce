"""
Rightmost Char
Challenge Description:
You are given a string 'S' and a character 't'. Print out the position of the
rightmost occurrence of 't' (case matters) in 'S' or -1 if there is none.
The position to be printed out is zero based.
Input sample:
The first argument will ba a path to a filename, containing a string and a
character, comma delimited, one per line. Ignore all empty lines in the input
file. E.g.

Hello World,r
Hello CodeEval,E

Output sample:

Print out the zero based position of the character 't' in string 'S', one per
line. Do NOT print out empty lines between your output.
E.g.
8
10
"""



import sys

with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        string, char = line.rstrip().split(',')
        print(string.rfind(char))