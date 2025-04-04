def square_ten_tree_decomposition(L, R):
    # Calculate the length of the segment
    segment_length = R - L + 1

    # Initialize variables
    level_sizes = []
    size = 1

    # Determine all possible level sizes
    while size <= segment_length:
        level_sizes.append(size)
        size *= 10

    # Initialize k to the last index of level_sizes
    k = len(level_sizes) - 1

    # List to store the decomposition result
    decomposition = []

    # Decompose the segment
    while segment_length > 0:
        size = level_sizes[k]
        if segment_length >= size:
            count = segment_length // size
            decomposition.append((k, count))
            segment_length -= count * size
        k -= 1

    # Output the result in the required format
    print(len(decomposition))
    for level, count in decomposition:
        print(level, count)




if __name__ == '__main__':
    l = int(input())
    r = int(input())
    square_ten_tree_decomposition(l, r)
