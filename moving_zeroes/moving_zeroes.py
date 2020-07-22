'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    nonZero = 0
    l = len(arr)

    for i in range(l):
        if arr[i] != 0:
            arr[nonZero] = arr[i]
            nonZero += 1

    while nonZero < l:
        arr[nonZero] = 0
        nonZero += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")