# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input().strip()
k = input().strip()

pattern = re.compile(f'(?=({re.escape(k)}))')  # Lookahead to handle overlapping matches
matches = list(pattern.finditer(s))

if not matches:
    print((-1, -1))
else:
    for match in matches:
        start = match.start(1)  # Group 1 contains our actual match
        end = start + len(k) - 1
        print((start, end))