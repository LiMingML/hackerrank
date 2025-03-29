import re


def is_valid_credit_card(number):
    # Rule 1: Must start with 4, 5, or 6
    if not re.match(r'^[456]', number):
        return False

    # Rule 2: Must contain exactly 16 digits (with optional hyphens)
    clean_number = number.replace('-', '')
    if len(clean_number) != 16 or not clean_number.isdigit():
        return False

    # Rule 3: Hyphens must be properly placed if present
    if '-' in number:
        if not re.match(r'^\d{4}(-\d{4}){3}$', number):
            return False

    # Rule 4: No more than 3 consecutive repeated digits
    if re.search(r'(\d)\1{3,}', clean_number):
        return False

    return True


n = int(input())
for _ in range(n):
    card = input().strip()
    print("Valid" if is_valid_credit_card(card) else "Invalid")