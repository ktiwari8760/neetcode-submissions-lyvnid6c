class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def calculate(a , b , sign):
            if sign == "+":
                return a + b
            if sign == "-":
                return b - a
            if sign == "*":
                return a * b
            if sign == "/":
                return int(b / a)
            return -1
        for ele in tokens:
            if ele in ["+" , "-" , "*" , "/"]:
                if len(stack) >= 2:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(calculate(a , b , ele))
            else:
                stack.append(int(ele))
        return stack[-1] if stack else -1