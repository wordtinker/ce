"""
READ MORE
CHALLENGE DESCRIPTION:

You are given a text. Write a program which outputs its lines according to the following rules:

If line length is ≤ 55 characters, print it without any changes.
If the line length is > 55 characters, change it as follows:
Trim the line to 40 characters.
If there are spaces ‘ ’ in the resulting string, trim it once again to the last space (the space should be trimmed too).
Add a string ‘... <Read More>’ to the end of the resulting string and print it.
INPUT SAMPLE:

The first argument is a file. The file contains a text.

For example:

Tom exhibited.
Amy Lawrence was proud and glad, and she tried to make Tom see it in her face -
but he wouldn't look.
Tom was tugging at a button-hole and looking sheepish.
Two thousand verses is a great many - very, very great many.
Tom's mouth watered for the apple, but he stuck to his work.
OUTPUT SAMPLE:

Print to stdout the text lines with their length limited according to the rules described above.

For example:

Tom exhibited.
Amy Lawrence was proud and glad, and... <Read More>
Tom was tugging at a button-hole and looking sheepish.
Two thousand verses is a great many -... <Read More>
Tom's mouth watered for the apple, but... <Read More>
CONSTRAINTS:

The maximum length of a line in the input file is 300 characters.
There cannot be more than one consequent space character in the input data.
"""

import sys

with open(sys.argv[1], 'r') as test_cases:
    for line in test_cases:
        line = line.strip()
        if len(line) <= 55:
            print(line)
        else:
            new_line = line[:40]
            blank = new_line.rfind(' ')
            if blank != -1:
                new_line = new_line[:blank]
            print(new_line + "... <Read More>")