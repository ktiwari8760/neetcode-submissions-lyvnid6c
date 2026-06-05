class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = 0
        counter = 0
        while right < len(nums)-1:
            farthest = 0
            for i in range(left , right+1):
                farthest = max(farthest , nums[i]+i)
            left = right + 1
            right = farthest
            counter +=1
        return counter