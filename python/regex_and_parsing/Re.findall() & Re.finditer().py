import re

def find_vowel_substrings(s):
    pattern = r'(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])'
    matches = re.findall(pattern, s, flags=re.IGNORECASE)
    return matches if matches else ['-1']

s = input().strip()
result = find_vowel_substrings(s)
print('\n'.join(result))