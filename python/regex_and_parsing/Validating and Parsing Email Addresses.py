# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

# Define regex pattern for a valid email address
email_pattern = re.compile(r'<[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>')

# Read input
n = int(input())

for _ in range(n):
    name, email = input().split()

    if email_pattern.fullmatch(email):
        print(name, email)