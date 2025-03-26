def average(array):
    # your code goes here
    s = set(array)
    return f"{sum(s) / len(s):.3f}"

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)