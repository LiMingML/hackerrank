import re

t = int(input())
pattern = r"^[+-]?[0-9]*\.[0-9]+$"
for _ in range(t):
    s = input()
    try:
        if re.fullmatch(pattern, s):
            float(s)
            print(True)
        else:
            print(False)
    except ValueError:
        print(False)
