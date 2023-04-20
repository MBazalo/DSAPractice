def isValid(s):
    opening = ['(', '[', '{']
    stack = []
    for bracket in s:
        if bracket in opening:
            stack.append(bracket)
        else:
            if stack:
                if (bracket == ')' and stack[-1] == '(') or (bracket == ']' and stack[-1] == '[') or (
                        bracket == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
            else:
                return False
    if stack:
        return False
    else:
        return True