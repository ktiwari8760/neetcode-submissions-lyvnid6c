class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_ = 0
        max_sum = float('-inf')
        for ele in nums:
            if sum_ < 0:
                sum_ = ele
            else:
                sum_ += ele
            max_sum = max(max_sum,sum_)
        return max_sum