# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = input()
lst = [(len(list(v)),int(k)) for k,v in groupby(s)]
print(*lst)

