# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
s = list(map(str, input().split()))
k = int(input())

com = list(combinations(s, k))
num = 0
for tup in com:
    if 'a' in tup:
        num += 1
res = num / len(com)
print(res)


