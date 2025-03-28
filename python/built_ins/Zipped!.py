# Enter your code here. Read input from STDIN. Print output to STDOUT
X, N = map(int, input().split())
scores = []
for _ in range(N):
    scores.append(list(map(float, input().split())))
scores = list(zip(*scores))
for score in scores:
    print(sum(score)/len(score))
