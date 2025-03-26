def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        dec_i = str(i)
        oct_i = oct(i)[2:]
        hex_i = hex(i).upper()[2:]
        bin_i = bin(i)[2:]
        print(dec_i.rjust(width),
              oct_i.rjust(width),
              hex_i.rjust(width),
              bin_i.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
