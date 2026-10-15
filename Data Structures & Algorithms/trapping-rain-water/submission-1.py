class Solution:
    def trap(self, height: List[int]) -> int:
        # Prefix maximum
        prefix_max = [0] * len(height)
        
        max_ele = 0
        for i , ele in enumerate(height):
            prefix_max[i] = max_ele
            max_ele = max(max_ele , ele)
        
        suffix_max = [0] * len(height)
        max_ele = 0
        for i  in range(len(height)-1 , -1 , -1):
            ele = height[i]
            suffix_max[i] = max_ele
            max_ele = max(max_ele , ele)

        answer = 0

        for i in range(len(height)):
            area = min(suffix_max[i] , prefix_max[i]) - height[i]
            if area > 0:
                answer += area
        return answer
        
        