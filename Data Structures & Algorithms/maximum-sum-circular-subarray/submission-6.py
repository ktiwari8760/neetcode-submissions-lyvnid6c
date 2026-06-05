class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]

        for i in range( len(nums)):
            current_sum = 0
            for j in range(i , len(nums)+i):
                j = j % len(nums)
                current_sum +=  nums[j]
                max_sum = max(max_sum , current_sum)
        return max_sum