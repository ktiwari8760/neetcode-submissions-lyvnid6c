class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ele in asteroids:
            flag = True
            while stack and stack[-1] > 0 and ele < 0: # Means both move opp
                if abs(stack[-1]) < abs(ele):
                    stack.pop()
                elif abs(stack[-1]) == abs(ele):
                    stack.pop()
                    flag = False
                    break
                else:
                    flag = False
                    break
            if flag:
                stack.append(ele)
        print(stack)
        return stack