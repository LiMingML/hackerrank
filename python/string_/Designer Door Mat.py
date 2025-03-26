# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    ele = ".|."
    for i in range(n//2):
        print((ele * (i*2+1)).center(m,'-'))
    print('WELCOME'.center(m,'-'))
    for i in range(n//2+1,n):
        print((ele*((n-i)*2-1)).center(m,'-'))
