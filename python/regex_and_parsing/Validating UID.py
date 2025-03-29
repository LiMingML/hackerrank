import re


def is_valid_uid(uid):
    # Rule 1: Exactly 10 characters
    if len(uid) != 10:
        return False

    # Rule 2: Only alphanumeric characters
    if not uid.isalnum():
        return False

    # Rule 3: At least 2 uppercase letters
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False

    # Rule 4: At least 3 digits
    if len(re.findall(r'\d', uid)) < 3:
        return False

    # Rule 5: No repeating characters
    if len(set(uid)) != len(uid):
        return False

    return True


n = int(input())
for _ in range(n):
    uid = input().strip()
    print("Valid" if is_valid_uid(uid) else "Invalid")