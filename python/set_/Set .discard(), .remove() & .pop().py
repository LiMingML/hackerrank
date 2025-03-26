n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    cmd_par = input().split()
    if cmd_par[0] == "pop":
        s.pop()
    if cmd_par[0] == "remove":
        s.remove(int(cmd_par[1]))
    if cmd_par[0] == "discard":
        s.discard(int(cmd_par[1]))
print(sum(s))
