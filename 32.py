# Valid Parentheses
def is_valid(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in "({[":
            stack.append(ch)               # opening bracket push karo
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False               # match nahi hua
    return len(stack) == 0                 # end me stack khali hona chahiye


# Tests
print(is_valid("({[]})"))   # True
print(is_valid("({[}])"))   # False
print(is_valid("("))        # False
print(is_valid(""))         # True