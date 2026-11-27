class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)

        max_so_far = 0

        for i in range(len(height)):
            left[i] = max_so_far
            max_so_far = max(max_so_far , height[i])
        

        right = [0] * len(height)

        
        max_so_far = 0

        for i in range(len(height)-1 , -1 , -1):
            right[i] = max_so_far
            max_so_far = max(max_so_far , height[i])
        water = 0
        for i in range(len(height)):
            water += max(0 , min(left[i] , right[i]) - height[i])
        return water
