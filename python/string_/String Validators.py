if __name__ == '__main__':
    s = input()
    lines = [False] * 5
    for c in s:
        if c.isalnum():
            lines[0] = True
        if c.isalpha():
            lines[1] = True
        if c.isdigit():
            lines[2] = True
        if c.isalpha() and c.islower():
            lines[3] = True
        if c.isalpha() and c.isupper():
            lines[4] = True

    for line in lines:
        print(line)
