if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    first_max = - 101
    second_max = -101
    for i in range(n):
        if arr[i] > first_max:
            second_max = first_max
            first_max = arr[i]
        if second_max < arr[i] < first_max:
            second_max = arr[i]
    print(second_max)


