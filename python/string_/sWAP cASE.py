def swap_case(s):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = s[i].lower()
        else:
            s[i] = s[i].upper()

    return "".join(s)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)