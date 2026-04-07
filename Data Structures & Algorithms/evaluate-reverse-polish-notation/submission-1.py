class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ele in tokens:
            if ele.isdigit():
                stack.append(ele)
            else:
                a = stack.pop()
                b = stack.pop()
                if ele == "+":
                    stack.append(int(a) + int(b))
                elif ele == "-":
                    stack.append(abs(int(a) - int(b)))
                elif ele == "*":
                    stack.append(int(a) * int(b))
                elif ele == "/":
                    stack.append(int(a) // int(b))
        return stack[0]