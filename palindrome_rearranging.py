'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] string inputString

    A string consisting of lowercase English letters.

    Guaranteed constraints:
    1 ≤ inputString.length ≤ 50.

    [output] boolean

    true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.


    How to determine is a word can be a palindrome
    ----------------------------------------------------
    https://www.geeksforgeeks.org/check-characters-given-string-can-rearranged-form-palindrome/
    A set of characters can form a palindrome if at most one character occurs odd number of times and all characters occur even number of times.


    https://stackoverflow.com/questions/31224628/check-if-a-permutation-of-a-string-can-become-a-palindrome

    So basically you want to determine if you can rearrange the characters of the input string into a palindrome? If so, then the answer is "yes" if 1) the length is even, and every unique character occurs a multiple of 2, or 2) the length is odd, and every unique character occurs a multiple of 2 except one
'''


def palindromeRearranging(inputString):
    '''
    Conditions to meet:

    1: the length is even, and every unique character occurs a multiple of 2
    2: the length is odd, and every unique character occurs a multiple of 2 except one
    '''
    can_convert_to_palindrome = True
    string_lenght = len(inputString)

    # Edge condition
    if string_lenght == 1:
        return True

    # Remove all duplicates. set() removes the duplicates, leaving just unique characters
    unique_characters = set(inputString)

    # Check all characters occur even number of time
    for i in unique_characters:
        times = inputString.count(i)
        if times % 2 != 0:
            can_convert_to_palindrome = False

    return can_convert_to_palindrome


print(palindromeRearranging("abca"))



