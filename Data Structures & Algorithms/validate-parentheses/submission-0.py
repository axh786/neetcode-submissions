class Solution:
    def isValid(self, s: str) -> bool:
        closeBracket = {")": "(", "}": "{", "]": "["}
        openBrackets = "({["
        stack = []

        for bracket in s:
            if bracket in openBrackets:
                stack.append(bracket)
            else:
                if not stack or closeBracket[bracket] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        if stack:
            return False
        
        return True
