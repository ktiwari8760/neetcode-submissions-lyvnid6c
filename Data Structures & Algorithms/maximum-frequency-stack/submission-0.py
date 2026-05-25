class FreqStack:

    def __init__(self):
        self.freqMap = {}
        self.maxFreq = 0
        self.stack = {}
    def push(self, val: int) -> None:
        newfreq = self.freqMap.get(val , 0) + 1
        self.freqMap[val] = newfreq
        if newfreq > self.maxFreq:
            self.maxFreq = newfreq
            self.stack[self.maxFreq] = []
        self.stack[self.freqMap[val]].append(val)
    def pop(self) -> int:
        res = self.stack[self.maxFreq].pop()
        self.freqMap[res] -= 1
        if not self.stack[self.maxFreq]:
            self.maxFreq -= 1
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()