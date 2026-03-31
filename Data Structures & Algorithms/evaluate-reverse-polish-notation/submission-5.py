class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for ele in tokens:
            if ele not in operators:
                stack.append(int(ele))
            else:
                a = stack.pop() 
                b = stack.pop() 
                if ele == "+":
                    stack.append(int(a) + int(b))
                elif ele == "-":
                    stack.append(int(b)-int(a))
                elif ele == "*":
                    stack.append(int(a) * int(b))
                elif ele == "/":
                    stack.append(int(float(b) / int(a)))
        return stack[0]