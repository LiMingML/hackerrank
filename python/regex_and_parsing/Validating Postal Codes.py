# Rule 1 and 2: 6 digits, 1-9 first
regex_integer_in_range = r'^[1-9]\d{5}$'  # Do not delete 'r'.
# Rule 3: Find alternating pairs
regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)' # Do not delete 'r'.

import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)