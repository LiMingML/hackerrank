# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k, m = map(int, input().split())

lsts = []
s_max = 0
for _ in range(k):
    lsts.append(list(map(int, input().split()))[1:])

prods = list(product(*lsts))
for i in prods:
    tmp = 0
    for j in range(k):
        tmp += i[j] ** 2
    tmp_mod = tmp % m
    if tmp_mod > s_max:
        s_max = tmp_mod
print(s_max)

