class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        min_ele = float('inf')
        while(left<= right):
            mid = (left+right)//2

            if(nums[left] <= nums[mid]):
                min_ele = min(min_ele , nums[left])
                left = mid+1
            elif (nums[right] >= nums[mid]):
                min_ele = min(min_ele , nums[mid])
                right = mid-1

        return min_ele