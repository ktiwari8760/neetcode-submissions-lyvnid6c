class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            flag = True
            current = asteroids[i]
            while stack and (stack[-1] > 0 and asteroids[i] < 0 ):
                top = stack[-1]
                if abs(top) < abs(current):
                    stack.pop()
                elif abs(top) == abs(current):
                    flag = False
                    stack.pop()
                    break
                elif abs(top) > abs(current):
                    flag = False
                    break
            print(current , flag)
            if flag:
                stack.append(current)
        return stack