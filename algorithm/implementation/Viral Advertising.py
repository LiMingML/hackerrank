#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
d = {}


def viralAdvertising(n):
    # Write your code here
    def helper(n):
        if n in d:
            return d[n]

        if n == 1:
            d[n] = 2
            return 2

        fn = math.floor(helper(n - 1) * 3 / 2)
        d[n] = fn
        return fn

    answer = 0
    for i in range(1, n + 1):
        answer += helper(i)
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
