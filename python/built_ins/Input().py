# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = map(int, input().split())
poly_exp = input()
print((eval(poly_exp))==k)  