class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        potential_min = float('inf')
        while(left <= right):
            mid = (left+right) // 2
            if nums[left] <= nums[mid]:
                potential_min = min(potential_min , nums[left])
                left = mid+1
            else:
                potential_min = min(potential_min , nums[mid])
                right = mid-1
        return potential_min