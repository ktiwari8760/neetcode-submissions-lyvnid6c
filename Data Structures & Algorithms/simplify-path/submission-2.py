class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for ele in path:
            if not ele or ele == ".":
                continue
            elif ele == "..":
                if stack:
                    stack.pop()
            elif ele.isalpha() or ele != "." or ele != "..":
                stack.append(ele)
        return "/" + "/".join(stack)

        