class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ele in tokens:
            if ele.isdigit():
                stack.append(ele)
            else:
                a = stack.pop() if stack else 0
                b = stack.pop() if stack else 0
                if ele == "+":
                    stack.append(int(a) + int(b))
                elif ele == "-":
                    stack.append(abs(int(a) - int(b)))
                elif ele == "*":
                    stack.append(int(a) * int(b))
                elif ele == "/":
                    if b != 0 :
                        stack.append(int(a) // int(b))
        return stack[0]