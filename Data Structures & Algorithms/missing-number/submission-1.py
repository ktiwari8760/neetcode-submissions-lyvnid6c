class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = 0

        for i in range(len(nums)):
            xorr ^= i ^ nums[i]
        
        xorr ^= len(nums)
        return xorr