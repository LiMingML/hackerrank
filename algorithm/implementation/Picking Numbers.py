#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    answer = 0
    for start in range(len(a) - 1):
        for end in range(start + 1, len(a)):
            if abs(a[end] - a[start]) <= 1:
                if end - start + 1 > answer:
                    answer = end - start + 1
            else:
                break
    return answer


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input().strip())
#
#     a = list(map(int, input().rstrip().split()))
#
#     result = pickingNumbers(a)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()

n = 6
a = list(map(int, '4 6 5 3 3 1'.split()))
print(pickingNumbers(a))
