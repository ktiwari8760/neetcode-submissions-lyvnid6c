class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        lst = list(zip(position , speed))
        lst.sort(key=lambda x : x[0])
        for i in range(len(lst)):
            while stack and stack[-1] <= ((target - lst[i][0]) / lst[i][1]):
                stack.pop()
            stack.append((target - lst[i][0]) / lst[i][1])
        return len(stack)