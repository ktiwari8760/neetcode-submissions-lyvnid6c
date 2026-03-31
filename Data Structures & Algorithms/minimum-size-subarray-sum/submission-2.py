class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum1 = 0
        min_val = float('inf')
        for right in range(len(nums)):
            print(sum1 , min_val , right , left)
            sum1 += nums[right]
            while(sum1 >= target):
                min_val = min(min_val , right-left+1)
                sum1 -= nums[left]
                left += 1
        
        return min_val if min_val != float("inf") else 0