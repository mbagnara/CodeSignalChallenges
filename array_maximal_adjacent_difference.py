def arrayMaximalAdjacentDifference(inputArray):

    # First element
    prev_value = inputArray[0]

    # list will store different between adjacent elements
    list_with_differences = []

    for k, v in enumerate(inputArray):

        '''
            First element has no previous value to compare with, so it is skipped
        '''
        if k == 0:
            continue

        diff = abs(v - prev_value)

        list_with_differences.append(diff)
        prev_value = v

    return max(list_with_differences)


a = [2, 4, -1, 0]
a = [1, 1, 1, 1]
a = [-1, 1, -3, -4]  # expected value: 4
a = [-2, -2, -2, -2, -2]
print(arrayMaximalAdjacentDifference(a))

