#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    common_length = 0
    min_len = min(len(s), len(t))

    # Find the length of the common prefix
    for i in range(min_len):
        if s[i] == t[i]:
            common_length += 1
        else:
            break

    total_operations = (len(s) - common_length) + (len(t) - common_length)

    # Case 1: We can perform the operations directly
    if k >= total_operations and (k - total_operations) % 2 == 0:
        return "Yes"
    # Case 2: We can delete all of s and build t from scratch
    elif k >= len(s) + len(t):
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
