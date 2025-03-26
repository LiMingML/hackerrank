#!/bin/python3

import math
import os
import random
import re
import sys
import collections


if __name__ == '__main__':
    s = input()
    counter = collections.Counter(sorted(s))
    top3 = counter.most_common(3)
    [print(*x) for x in top3]
