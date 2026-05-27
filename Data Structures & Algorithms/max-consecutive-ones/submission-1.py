class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counter = 0
        local_counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                local_counter += 1
            else:
                max_counter = max(max_counter , local_counter)
                local_counter = 0
        max_counter = max(max_counter , local_counter)
        return max_counter 