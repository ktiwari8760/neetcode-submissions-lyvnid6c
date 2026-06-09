class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        local_sum = 0
        for i , ele in enumerate(nums):
            right_sum = total_sum-local_sum - ele
            if local_sum == right_sum:
                return i
            local_sum += ele
        return -1
