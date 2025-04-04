#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
def is_leap(year):
    return (year < 1918 and year % 4 == 0) or (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)))


def dayOfProgrammer(year):
    # Write your code here
    if year == 1918:
        return "26.09.1918"
    elif is_leap(year):
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
