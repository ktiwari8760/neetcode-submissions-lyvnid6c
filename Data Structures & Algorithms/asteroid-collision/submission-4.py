class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in range(len(asteroids)):
            ele = asteroids[i]
            alive = True
            while(alive and stack and stack[-1] > 0 and ele < 0):
                if abs(stack[-1]) == abs(ele):
                    alive = False
                    stack.pop()
                elif stack[-1] < -ele:
                    stack.pop()
                else:
                    alive = False
            if alive:
                stack.append(ele)
        return stack