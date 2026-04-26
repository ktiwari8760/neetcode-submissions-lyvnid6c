class Solution:
    def isValid(self, s: str) -> bool:
        open_braces = ["{" , "(" , "["]
        stack = []
        for i in range(len(s)):
            if s[i] in open_braces:
                stack.append(s[i])
            elif not stack:
                return False
            else:
                popped = stack.pop()
                if s[i] == "}" and popped != "{":
                    return False
                if s[i] == "]" and popped != "[":
                    return False
                if s[i] == ")" and popped != "(":
                    return False
        return len(stack) == 0
