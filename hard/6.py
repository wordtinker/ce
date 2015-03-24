"""
Longest Common Subsequence
Challenge Description:

You are given two sequences. Write a program to determine the longest common 
subsequence between the two strings (each string can have a maximum length of 
50 characters). NOTE: This subsequence need not be contiguous. The input file 
may contain empty lines, these need to be ignored.
Input sample:
The first argument will be a path to a filename that contains two strings per 
line, semicolon delimited. You can assume that there is only one unique 
subsequence per test case. E.g.

XMJYAUZ;MZJAWXU
Output sample:
The longest common subsequence. Ensure that there are no trailing empty spaces 
on each line you print. E.g.
MJAU
"""


import sys

def assemble(string_a, string_b, table, i, j):
    if table[i][j] == 0:
        return ''

    if string_a[i - 1] == string_b[j - 1]:
        return assemble(string_a, string_b, table, i - 1, j - 1) + string_a[i - 1]
    elif table[i - 1][j] > table[i][j - 1]:
        return assemble(string_a, string_b, table, i - 1, j)
    else:
        return assemble(string_a, string_b, table, i, j - 1)

def get_subsequence(string_a, string_b):

    # Build the initial table
    # we need +1 so can keep track of LCS of '' and the rest of the other string
    table = []
    for i in range(len(string_a) + 1):
        table.append([0] * (len(string_b) + 1))


    # Build the table from left to right, top to bottom
    for i, let_left in enumerate(string_a):
        for j, let_right in enumerate(string_b):
            if let_left == let_right:
                # LCS is growing
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])

    return assemble(string_a, string_b, table, len(string_a), len(string_b))


with open(sys.argv[1]) as file:
    for line in file:
        l = line.rstrip()
        if l:
            a, b = line.split(';')
            print(get_subsequence(a, b))

# print(get_subsequence('GQTZBFUTLY', 'HEIBMUXTHVCMOJYOUUHF'))


