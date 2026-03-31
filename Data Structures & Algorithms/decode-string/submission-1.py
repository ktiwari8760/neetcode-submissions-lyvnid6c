class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        answer = ""
        for i , ele in enumerate(s):
            if ele == "]":
                curr = ""
                while(stack[-1] != "["):
                    curr = stack.pop() + curr
                stack.pop()
                k = ""
                while(stack and stack[-1].isdigit()):
                    k = stack.pop() + k
                freq = int(k) * curr
                stack.append(freq)
            else:
                stack.append(ele)
        return "".join(stack)