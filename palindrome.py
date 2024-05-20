"""Module providing a function checking if string is palindrome."""
from collections import deque

def is_palindrome(s):
    """Function checking if string is palindrome"""
    s = ''.join(filter(str.isalnum, s)).lower()
    dq = deque(s)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            print(f'"{input_string}" is not palindrome')
            return False
    print(f'"{input_string}" is palindrome')
    return True

# Usage
input_string = "A man a plan a canal Panama"
is_palindrome(input_string)
