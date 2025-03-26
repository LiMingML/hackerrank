# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

d = OrderedDict()

n = int(input())
for _ in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(len(d))
print(*[v for k, v in d.items()])

