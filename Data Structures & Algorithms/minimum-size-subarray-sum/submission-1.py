class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_val = float('inf')
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i , len(nums)):
                curr_sum += nums[j]

                if curr_sum >= target:
                    min_val = min(min_val , j-i+1)
                    break
        return min_val if min_val != float('inf') else 0