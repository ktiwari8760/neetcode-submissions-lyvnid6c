class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        middle = 0
        right = len(nums)-1

        while(middle <= right):
            ele = nums[middle]

            if ele == 0:
                nums[left] , nums[middle] = nums[middle] , nums[left]
                left += 1
                middle += 1
            elif ele == 1:
                middle += 1
            else:
                nums[right] , nums[middle] = nums[middle] , nums[right]
                right -= 1
        return nums