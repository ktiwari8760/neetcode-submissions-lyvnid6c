class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        actual_sum = int(n * (n+1)/2)
        array_sum = sum(nums)

        return actual_sum - array_sum