class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == "{":
                stack.append(ch)
            elif ch == "[":
                stack.append(ch)
            elif ch == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif ch == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif ch == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                continue
        return len(stack) == 0
