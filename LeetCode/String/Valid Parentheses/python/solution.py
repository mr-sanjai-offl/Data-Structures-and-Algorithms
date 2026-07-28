class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                last = stack[-1]
                if (last == '(' and i != ')') or (last == '[' and i != ']') or (last == '{' and i != '}'):
                    return False
                stack.pop()
        return not stack