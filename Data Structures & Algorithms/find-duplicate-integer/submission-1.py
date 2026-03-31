class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        while(left < len(nums)-1):
            if nums[left] == nums[left+1]:
                return nums[left]
            left += 1
        return -1