class FreqStack:

    def __init__(self):
        self.stack = {} # This will be the freq : []
        self.maxFreq = 0
        self.freq = {}
    def push(self, val: int) -> None:
        # We have to push the element first 
        updated_freq = self.freq.get(val , 0) + 1
        self.freq[val] = updated_freq
        if updated_freq > self.maxFreq:
            self.maxFreq = updated_freq
            self.stack[self.maxFreq] = []
        self.stack[self.freq[val]].append(val)
    def pop(self) -> int:
        # While popping
        res = self.stack[self.maxFreq].pop()
        self.freq[res] -= 1
        if not self.stack[self.maxFreq]:
            self.maxFreq -= 1
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()