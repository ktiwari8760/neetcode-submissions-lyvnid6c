class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = nums[0]
        max_answer = nums[0]
        for i in range(1 , len(nums)):
            if nums[i] > nums[i-1]:
                answer += nums[i]
            else:
                answer = nums[i]
            max_answer = max(answer , max_answer)
        return max_answer