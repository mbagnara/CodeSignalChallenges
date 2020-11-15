'''
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

    For a = [1, 2, 3] and b = [1, 2, 3], the output should be
    areSimilar(a, b) = true.

    The arrays are equal, no need to swap any elements.

    For a = [1, 2, 3] and b = [2, 1, 3], the output should be
    areSimilar(a, b) = true.

    We can obtain b from a by swapping 2 and 1 in b.

    For a = [1, 2, 2] and b = [2, 1, 1], the output should be
    areSimilar(a, b) = false.

    Any swap of any two elements either in a or in b won't make a and b equal.
'''

# This code would pass only 19 out of 20 cases
def areSimilar(a, b):

    # Count swaps
    swap_count = 0

    for k, v in enumerate(a):

        if v != b[k]:

            # Swapping is allowed only once. If differences are found more than one then, it has to False.
            if swap_count > 0:
                return False

            # Search v in b[]. If the value is not found an exception is raised. -1: not found
            try:
                # Found value in list b
                found_at = b.index(v, k)

                # Swap values to leave both list positions the same
                if b[k] == a[found_at]:
                    b[found_at] = b[k]
                    b[k] = v
                    swap_count += 1
                else:
                    return False

            except ValueError:
                return False   # value is not found in code line: found_at = b.index(v, k)

    return True


'''
This functions will identify all different pairs betweens lists a and b
if count = 0, means all pairs are the same. Therefore, the result is True
if count== 2, means more than one pair is different
    if duplicates
'''
def areSimilar2(a, b):
    count = 0
    list_a = []
    list_b = []

    # Find differences between lists a and b
    for i in range(len(a)):

        if (a[i] != b[i]):
            count += 1
            list_a.append(a[i])
            list_b.append(b[i])

    print(f"a: {a}, list_a: {list_a}, set(list_a): {set(list_a)}")
    print(f"b: {b}, list_b: {list_b}, set(list_b): {set(list_b)}")

    if (count == 0):
        print("count 0")
        return True

    elif count == 2:
        print("count 2", set(list_a) == set(list_b))
        # SET removes the duplicates
        return set(list_a) == set(list_b)

    else:
        print(f"count {count}")
        return False


a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]
print("Case:", areSimilar2(a, b))


# # First case: True
# a = [1, 2, 3]
# b = [1, 2, 3]

# print("First case, expected True", areSimilar(a, b))


# # Second case: True
# a = [1, 2, 3]
# b = [2, 1, 3]

# print("Second case case, expected True", areSimilar(a, b))


# # Third case: False
# a = [1, 2, 2]
# b = [2, 1, 1]

# print("Third case, expected False and returned", areSimilar(a, b))


# # Fourth case: True
# a: [2, 3, 1]
# b: [1, 3, 2]

# print("Fourth case, expected: True, but got", areSimilar(a, b))

# # Final case: True
# a: [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
# b: [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]

# print("Final case, expected: False, but got", areSimilar(a, b))

