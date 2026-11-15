class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, val: int) -> None:
        # We push simply in stack 
        self.stack.append(val)

        # we maintain a minstack 
        if (not self.minstack or self.minstack[-1] >= val):
            self.minstack.append(val)
    def pop(self) -> None:
        if not self.stack:
            return 
        if self.stack[-1] == self.minstack[-1]:
            self.stack.pop()
            self.minstack.pop()
        else:
            self.stack.pop()
        return
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1
    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        return -1
        
