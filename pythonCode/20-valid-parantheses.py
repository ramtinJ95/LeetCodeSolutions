
def isValid(s: str) -> bool:
    if len(s) % 2 == 1:
        return False

    stack = []
    mapping = {"]":"[","}":"{",")":"("}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False