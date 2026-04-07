class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(i):
            if i >= len(nums):
                return 0
            if i < 0:
                return 0
            return max(helper(i-1) , (nums[i] + helper(i-2)))
        return helper(len(nums)-1) 