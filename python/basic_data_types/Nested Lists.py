import collections
import sys

if __name__ == '__main__':

    lowest = sys.float_info.max
    second_lowest = sys.float_info.max
    d = collections.defaultdict(list)

    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[score].append(name)
        if score < lowest:
            second_lowest = lowest
            lowest = score
        if lowest < score < second_lowest:
            second_lowest = score

    names = sorted(d[second_lowest])
    for i in names:
        print(i)



