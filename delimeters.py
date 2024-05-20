def check_delimiters(s):
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
