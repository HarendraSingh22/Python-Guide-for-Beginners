# Program to check if the input string is palindrome or not. e.g isPalindrome('ABCBA') => True
# Written on Python 3.6.2
from math import floor, ceil


def isPalindrome(str):
    # Use stack to add the first half characters of the string
    # In python, we can use list as a stack
    stack = list()

    # add the first half into the stack, ignore the middle one if the length is odd
    # if len(str) = 5 then half position is 2
    # else if len(str) = 4 then half position is also 2
    first_half_position = int(floor(len(str) / 2))
    for i in range(0, first_half_position):
        stack.append(str[i])
    # pop the second half from the stack, ignore the middle one if the length is odd
    # if len(str) = 5 then half position is 3
    # else if len(str) = 4 then half position is also 3
    second_half_position = int(ceil(len(str) / 2))
    for i in range(second_half_position, len(str)):
        # pop the last element of the stack then check if equal to str[i]
        char = stack.pop()
        if char != str[i]:
            # if not equal, then not palindrome
            return False

    # if the stack is empty, then the str is palindrome
    if len(stack) == 0:
        return True
    return False
