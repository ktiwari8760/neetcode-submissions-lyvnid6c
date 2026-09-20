class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ele in s:
            if ele in ["{" , "[" , "("]:
                stack.append(ele)
            else:
                if not stack:
                    return False
                popped = stack.pop()
                if ele == "}" and popped != "{":
                    return False
                if ele == "]" and popped != "[":
                    return False
                if ele == ")" and popped != "(":
                    return False
        return len(stack) == 0