# Enter your code here. Read input from STDIN. Print output to STDOUT
print(''.join(sorted(input().strip(), key=lambda c: (
    0 if c.islower() else
    1 if c.isupper() else
    2 if c.isdigit() and int(c) % 2 else
    3, c))))
