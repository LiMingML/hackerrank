# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
n = int(input())
result = True
for _ in range(n):
    B = set(map(int, input().split()))
    if B.issubset(A):
        if A.issubset(B):
            result = False
    else:
        result = False
print(result)
