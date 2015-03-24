"""
Print the size of a file in bytes
"""

import sys
import os

stats = os.stat(sys.argv[1])
print(stats.st_size)
