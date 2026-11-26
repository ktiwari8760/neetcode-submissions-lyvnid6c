class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # We replace all negative numbers by 0

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            value = abs(nums[i])
            if 1 <= value <= len(nums):
                if nums[value-1] > 0:
                    nums[value-1] *= -1
                elif nums[value-1] == 0:
                    nums[value-1] = -1 * (len(nums)+1)
        
        for i in range(0 , len(nums)):
            if nums[i] >= 0:
                return i+1
        return len(nums)+1