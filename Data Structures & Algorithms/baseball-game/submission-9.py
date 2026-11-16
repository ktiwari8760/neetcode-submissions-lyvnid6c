class Solution:
    def calPoints(self, operations: List[str]) -> int:
        

        stack = []

        for i in range(len(operations)):
            # We take the elements and if it's a number we simply append it to stack 
            ele = operations[i].lstrip('-')
            if ele.isdigit():
                stack.append(int(operations[i]))
            else:
                if operations[i] == "+":
                    if len(stack) >= 2:
                        first = stack[-1]
                        second = stack[-2]
                        third = first+ second
                        stack.append(third)
                    else:
                        continue
                if operations[i] == "D":
                    if len(stack) >= 1:
                        stack.append(stack[-1] * 2)
                if operations[i] == "C":
                    if stack:
                        stack.pop()
        return sum(stack)