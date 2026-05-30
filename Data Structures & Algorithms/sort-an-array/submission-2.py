class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def helper(nums):
            if len(nums) <= 1:
                return nums
            pivot = len(nums) // 2
            pivot_ele = nums[pivot]

            left = []
            right = []
            middle = []

            for ele in nums:
                if ele < pivot_ele:
                    left.append(ele)
                elif ele > pivot_ele:
                    right.append(ele)
                else:
                    middle.append(ele)
            return helper(left) + middle + helper(right)
        return helper(nums)