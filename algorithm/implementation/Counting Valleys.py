#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    valley_count = 0

    for step in path:
        if step == 'U':
            altitude += 1
            # Check if we just came up to sea level
            if altitude == 0:
                valley_count += 1
        else:  # 'D'
            altitude -= 1

    return valley_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # steps = int(input().strip())
    #
    # path = input()
    #
    # result = countingValleys(steps, path)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
    steps = 8
    path = "UDDDUDUU"
    print(countingValleys(steps, path))