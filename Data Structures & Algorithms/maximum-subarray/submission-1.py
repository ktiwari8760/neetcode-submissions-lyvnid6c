class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        sum_ = 0
        max_sum = float('-inf')
        while(right < len(nums)):
            sum_ += nums[right]

            max_sum = max(max_sum , sum_)

            while sum_ < 0:
                sum_ -= nums[left]
                left += 1
            right += 1
        return max_sum