class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ele in s:
            if ele in {"(" , "{" , "["}:
                stack.append(ele)
            else:
                if len(stack) > 0:
                    last_ele = stack.pop()
                    if last_ele == "(" and ele != ")":
                        return False
                    elif last_ele == "{" and ele != "}":
                        return False
                    elif last_ele == "[" and ele != "]":
                        return False
                else:
                    return False # We are closing bracket before it's being oopened

        return True