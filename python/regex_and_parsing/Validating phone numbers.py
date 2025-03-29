# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def validate_phone_number(number):
    pattern = r'^[789]\d{9}$'
    return "YES" if re.fullmatch(pattern, number) else "NO"

n = int(input())
for _ in range(n):
    phone_num = input().strip()
    print(validate_phone_number(phone_num))
