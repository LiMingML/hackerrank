# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


hex_pattern = re.compile(r'(#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b)')

n = int(input())  # Read the number of input lines
css_lines = [input().strip() for _ in range(n)]  # Read all input lines

inside_braces = False  # Track whether we are inside a CSS block

# TODO: {}在一行；判断在{}之中的代码需要优化
for line in css_lines:
    # Check if we enter or exit a CSS block
    if '{' in line:
        inside_braces = True
    elif '}' in line:
        inside_braces = False

    # Extract hex color codes only when inside a CSS block
    if inside_braces:
        matches = hex_pattern.finditer(line)
        for match in matches:
            if '{' in line:
                if line.index('{') < match.start(1):
                    print(match.group(1))
            else:
                print(match.group(1))
