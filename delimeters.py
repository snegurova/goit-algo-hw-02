"""Module providing a function checking if delimiters are symmetric."""

def check_delimiters(s):
    """Function checking if delimiters are symmetric"""
    stack = []
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if stack and stack[-1] == matches[char]:
                stack.pop()
            else:
                return "Is not symmetric"

    return "Is symmetric" if not stack else "Is not symmetric"

# Usage
test_strings = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for ts in test_strings:
    result = check_delimiters(ts)
    print(f'"{ts}": {result}')
