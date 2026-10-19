class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        left = [-1] * len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop() # we can extend till here
            if stack:
                left[i] = stack[-1]
            stack.append(i)
        
        stack = []
        n = len(heights)
        right = [n] * n

        for i in range(n-1 , -1 , -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop() # we can extend till here
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        max_area = 0
        for i in range(n):
            left[i] += 1
            right[i] -= 1
            area = heights[i] * (right[i] - left[i] + 1)
            max_area = max(max_area , area)
        return max_area

