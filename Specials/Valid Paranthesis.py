def valid_parentheses(s):
    stack = []
    map = {')':'(','}':'{',']':'['}

    for i in s:
        if i in map.values():
            stack.append(i)
        elif i in map:
            if not stack or stack[-1] != map[i]:
                return False
            stack.pop()
        else:
            return False
    return not stack

s = "()"
print(valid_parentheses(s))