class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path + "/"
        stack = []
        num = ""
        i = 0
        while(i < len(path)):
            if path[i] == "/":
                if num == "..":
                    if stack:
                        stack.pop()
                elif num != "." and num != "":
                    stack.append(num)
                num = ""
            else:
                num += path[i]
            i += 1
        return "/" + "/".join(stack)
