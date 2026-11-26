class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        
        for right in range(0 ,  len(nums)):
            if right < len(nums)-1 and nums[right] == nums[right+1]:
                continue
            nums[left] , nums[right] = nums[right] , nums[left]
            left += 1
        return left