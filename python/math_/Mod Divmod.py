# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = int(input())
result = divmod(a,b)
print(result[0], result[1], result, sep='\n')
