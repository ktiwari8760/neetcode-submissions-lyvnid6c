class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def time(position , speed):
            return (target-position)/speed
        cars = sorted(zip(position , speed) , reverse = True)
        stack = []

        for pos,spd in cars:
            currenttime = time(pos,spd)
            if stack and stack[-1] >= currenttime:
                continue
            stack.append(currenttime)
        return len(stack)