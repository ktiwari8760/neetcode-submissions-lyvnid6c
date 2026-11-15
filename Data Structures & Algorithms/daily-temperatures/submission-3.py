class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = []
        for i in range(len(temperatures)-1 , -1 , -1):
            if not stack:
                stack.append((temperatures[i] , i))
                result.append(0)
                continue
            else:
                while stack and stack[-1][0] <= temperatures[i]:
                    stack.pop()
                next_greater = 0
                if stack:
                    next_greater = stack[-1][1] - i
                result.append(next_greater)
                stack.append((temperatures[i] , i))
        return result[::-1]
                