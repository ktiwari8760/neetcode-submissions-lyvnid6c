class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump_possible = 0

        for i in range(len(nums)):
            if i > max_jump_possible:
                return False
            max_jump_possible = max(max_jump_possible , nums[i]+i)
        return True