class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Finding the minmum in the rotated sorted array 
        left = 0
        right = len(nums)-1
        answer = float('inf')
        while(left <= right):
            mid = (left + right)//2

            # If left part is sorted means arr[left] <= arr[mid]
            if nums[left] <= nums[mid]:
                answer = min(answer , nums[left])
                left = mid+1
            else:
                answer = min(answer , nums[mid])
                right = mid-1
        return answer