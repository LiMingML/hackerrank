# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
A = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    cmd = input().split()[0]
    s = set(map(int, input().split()))
    getattr(A, cmd)(s)
print(sum(A))
