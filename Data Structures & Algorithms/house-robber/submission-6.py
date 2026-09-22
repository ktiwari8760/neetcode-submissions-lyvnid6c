class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        amt = [0] * len(nums)
        amt[0] = nums[0]
        amt[1] = max(nums[0] , nums[1])
        for i in range(2 , len(nums)):
            amt[i] = max(amt[i-1] , nums[i] + amt[i-2])
        return amt[-1]