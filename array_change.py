
'''
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
'''


def arrayChange(inputArray):
    moves = 0

    # Gets the first element [0] to use as the prev_value from position 1 and ahead
    prev_value = inputArray[0]

    for k, v in enumerate(inputArray):

        # Skips 1st element [0]
        if k == 0:
            continue

        # Checks all elements from position [1] and ahead
        if v <= prev_value:
            new_value = prev_value + 1
            inputArray[k] = new_value
            moves += (new_value - v)

        prev_value = inputArray[k]

    return moves

# arrayChange([0, 1])
# arrayChange([1, 1])
# arrayChange([2, 1])
# arrayChange([3, 1])
# arrayChange([4, 1])

# arrayChange([1, 1])
# [1, 1, 1]
# print(arrayChange([1]))
# print(arrayChange([1, 1, 1]))
# print(arrayChange([2, 1, 10, 1]))
# print(arrayChange([-1000, 0, -2, 0]))
print(arrayChange([-1000, 0, -2, 0]))



