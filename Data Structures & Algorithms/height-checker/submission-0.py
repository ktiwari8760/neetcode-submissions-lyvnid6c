class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_height = sorted(heights)
        print(heights)
        print(sorted_height)
        left = 0
        right = 0
        counter = 0

        for i in range(len(heights)):
            if heights[i] != sorted_height[i]:
                counter += 1
        return counter