def print_rangoli(size):
    # your code goes here
    n = ord("a")
    alphabet = [chr(n+i) for i in range(size)]
    length = ((size*2)-1)*2 -1
    lst = list(range(size-1,-1,-1)) + list(range(1,size))
    for i in lst:
        right_side = alphabet[i:]
        left_side = right_side[::-1][:-1]
        line = left_side + right_side
        line = "-".join(line).center(length, "-")
        print(line)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)