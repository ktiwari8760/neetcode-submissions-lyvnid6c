class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for ele in nums[1:]:
            current_sum = max(current_sum + ele , ele)
            max_sum = max(max_sum , current_sum)
        return max_sum