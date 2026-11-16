class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ele in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and ele < 0:
                if stack[-1] == -ele:
                    alive = False
                    stack.pop()
                elif stack[-1] > -ele:
                    alive = False
                else:
                    stack.pop()
            
            if alive:
                stack.append(ele)
        return stack 