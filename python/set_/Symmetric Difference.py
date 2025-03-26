# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    m = int(input())
    M = set(map(int, input().split()))
    n = int(input())
    N = set(map(int, input().split()))
    diff = M.difference(N).union(N.difference(M))
    diff_lst = sorted(list(diff))

    for i in diff_lst:
        print(i)

