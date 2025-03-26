# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n = int(input())
    s = set()
    for _ in range(n):
        s.add(input())
    print(len(s))
