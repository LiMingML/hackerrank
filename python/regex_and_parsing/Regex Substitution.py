# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def substitute_operators(text):
    # Pattern for && with word boundaries
    and_pattern = r'(?<=\s)&&(?=\s)'
    # Pattern for || with word boundaries
    or_pattern = r'(?<=\s)\|\|(?=\s)'

    # Substitute && first, then ||
    text = re.sub(and_pattern, 'and', text)
    text = re.sub(or_pattern, 'or', text)
    return text


n = int(input())
for _ in range(n):
    line = input()
    print(substitute_operators(line))
