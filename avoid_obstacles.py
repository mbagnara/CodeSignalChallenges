'''
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.
'''

def avoidObstacles(inputArray):

    print(inputArray)

    elements = len(inputArray)

    # Jumps to check
    for jump in range(1, 10000):

        jumps = 0

        # Check each element of the list
        for a in inputArray:

            # Valid jump
            if a % jump != 0:
                jumps += 1

        # JUMP works for all the elements of the list
        if elements == jumps:
            print(f"Jump FOUND: {jump}")
            return jump

    return jump


inputArray = [5, 3, 6, 7, 9]  # 4
avoidObstacles(inputArray)


inputArray = [19, 32, 11, 23]    # 3
avoidObstacles(inputArray)

inputArray = [5, 8, 9, 13, 14]   # 6
avoidObstacles(inputArray)
