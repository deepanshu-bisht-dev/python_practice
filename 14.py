def is_valid_brackets(s: str) -> bool:
    # Map closing brackets to their corresponding opening brackets
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in bracket_map:
            # Pop the top element from the stack if it's not empty, else assign a dummy value
            top_element = stack.pop() if stack else '#'
            
            # If the mapping doesn't match the stack's top element, it's invalid
            if bracket_map[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it onto the stack
            stack.append(char)

    # If the stack is empty, all brackets were properly closed
    return not stack

# Test Cases
print(is_valid_brackets("{[]}"))      # Output: True
print(is_valid_brackets("([)]"))      # Output: False
print(is_valid_brackets("(?]"))       # Output: False
