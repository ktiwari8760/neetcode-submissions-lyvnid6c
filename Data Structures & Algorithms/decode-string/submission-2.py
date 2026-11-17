class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        # We move in reverse order
        for i in range(len(s)-1 , -1 , -1):
            ele = s[i]

            if ele == "[":
                alpha= ""
                while stack and stack[-1] != "]":
                    alpha += stack.pop()
                stack.pop()
                j = i-1
                length = ""
                while i >= 0 and s[j].isdigit():
                    length += s[j]
                    j -= 1
                length = int(length[::-1])
                stack.append(length*alpha)
            elif ele.isdigit():
                continue 
            else:
                stack.append(ele)
        return "".join(stack[::-1]) if stack else ""
