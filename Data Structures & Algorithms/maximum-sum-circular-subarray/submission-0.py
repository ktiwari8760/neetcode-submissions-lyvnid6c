class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # How to handle circular subarrray

        n = len(nums)
        max_sum = float('-inf')
        for i in range(n):
            curr_sum = 0
            for j in range(i , i+n):
                curr_sum += nums[j % n ]
                max_sum = max(max_sum , curr_sum)
        return max_sum