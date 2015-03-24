"""
Sequence Transformation

Challenge Description:

There are two sequences. The first sequence consists of digits "0" and "1", the
second one consists of letters "A" and "B". The challenge is to determine
whether it's possible to transform a given binary sequence into a string
sequence using the following rules:
1. "0" can be transformed into non empty sequence of letters "A" ("A", "AA",
"AAA" etc.)
2. "1" can be transformed into non empty sequence of letters "A" ("A", "AA",
"AAA" etc.) or to non empty sequence of letters "B" ("B", "BB", "BBB" etc) e.g.
Input sample:
1010 AAAAABBBBAAAA
00 AAAAAA
01001110 AAAABAAABBBBBBAAAAAAA
1100110 BBAABABBA

Your program should accept as its first argument a path to a filename. Each
line in this file contains a binary sequence and a sequence of letters "A" and
"B" separated by a single whitespace. E.g.
Output sample:
Yes
Yes
Yes
No
For each test case print out "Yes" if the transformation is possible, otherwise
print "No". E.g.

Constraints:
The length of a binary sequence is in range [1, 150]
The length of a string sequence is in range [1, 1000]
The number of test cases is <= 50

[23:03:47] Al Zhukov: look at sequence of 1 and 0 and string of A and B
[23:03:47] Al Zhukov: and lets made cut seq[ i: ] and string[ j: ]
[23:04:45] Al Zhukov: and lets try to find the cost of transformation seq->string
[23:05:22] Al Zhukov: 0->A cost 0
[23:05:27] Al Zhukov: 1->B cost 0
[23:05:37] Al Zhukov: 1->A cost 0
[23:06:01] Al Zhukov: 0->B cost is Inf
[23:06:37] Al Zhukov: delettion of A if the we have 0 at i cut is 0
[23:06:55] Al Zhukov: delettion of any character if we have 1 at i cut is 0
[23:07:13] Al Zhukov: anythin else is Inf
[23:07:59] Al Zhukov: if we could find that of all possible transformations
there is one that cost 0 overall we can tranfrom seq into string
[23:11:46] Al Zhukov: does that make sense?
[23:12:37] Ophir: i don't understand the deletion stuff
[23:12:47] Al Zhukov: ok
[23:13:06] Al Zhukov: consider we have cuts at i and j
[23:13:27] Al Zhukov: if we have 0 and A we have 2 options
[23:13:49] Al Zhukov: if the next char is A we can delete A at no cost
[23:14:02] Al Zhukov: and return func(i, j+1)
[23:14:38] Al Zhukov: other option is to say we have to stop here and see at the
next number
[23:14:57] Al Zhukov: and return func(i+1, j+1)
[23:15:22] Al Zhukov: since our 0 can produce A, AA, AAA etc
[23:16:08] Al Zhukov: as we have both of these options we should return
min(func(i, j+1), func(i+1, j+1))
[23:16:59] Al Zhukov: if the next letter differs we have to abrupt our number
here and just return func(i+1, j+1)
"""

import sys

memo = {}

def memoize(func):

    def f(seq, string, i, j):
        if (i, j) not in memo:
            memo[(i, j)] = func(seq, string, i, j)

        return memo[(i, j)]

    return f


@memoize
def dp(seq, string, i, j):
    if i < len(seq) and j < len(string):
        if seq[i] == '0' and string[j] == 'A' or seq[i] == '1':
            if j + 1 < len(string) and string[j] == string[j+1]:
                return min(
                    dp(seq, string, i, j+1),  # Consume letter
                    dp(seq, string, i+1, j+1)  # Consume both letter and number
                )
            else:
                return dp(seq, string, i+1, j+1)  # Consume both letter and number
    elif i >= len(seq) and j >= len(string):
        return 0

    return float('inf')


with open(sys.argv[1]) as file:
    for test in file:
        test = test.rstrip()
        seq, string = test.split(' ')
        memo.clear()
        result = 'Yes' if dp(seq, string, 0, 0) == 0 else 'No'
        print(result)



# seq, string = '1010', 'AAAAABBBBAAAA'
# seq, string = '00', 'AAAAAA'
# seq, string = '01001110', 'AAAABAAABBBBBBAAAAAAA'
# seq, string = '1100110', 'BBAABABBA'
# result = dp(seq, string, 0, 0)
# print(result)