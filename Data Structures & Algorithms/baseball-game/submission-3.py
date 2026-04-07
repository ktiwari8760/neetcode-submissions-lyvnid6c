# Stack are nothing but a data structure which are like lists only but follow


#LIFO --> Last In first out
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] # Why we thought of using stack because we have to check for prrevious two
        for ele in operations:
            if ele.isdigit():
                stack.append(int(ele))
            elif ele == "+" :
                x = stack[-1]
                y = stack[-2]
                stack.append(x+y)
            elif ele == "D" :
                x = stack[-1]
                stack.append(x*2)
            elif ele == "C" :
                stack.pop()
        return sum(stack)