# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

string, k = input().split()
string = sorted(string)
k = int(k)

lst = list(combinations_with_replacement(string, k))

for j in lst:
    print("".join(j))

