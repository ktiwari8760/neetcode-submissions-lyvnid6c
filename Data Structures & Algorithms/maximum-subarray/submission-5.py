class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_Sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum+num)
            max_Sum = max(max_Sum , current_sum)
        return max_Sum
        