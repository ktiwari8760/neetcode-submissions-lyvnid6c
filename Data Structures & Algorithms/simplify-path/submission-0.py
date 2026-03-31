class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path+"/"
        stack = []
        i = 0
        name = ""
        while(i < len(path)):
            if path[i] == "/":
                if name == "..":
                    if stack:
                        stack.pop()
                elif name != "" and name != ".":
                    stack.append(name)
                name = ""
            else:
                name += path[i]
            i += 1
        return "/"+"/".join(stack)
