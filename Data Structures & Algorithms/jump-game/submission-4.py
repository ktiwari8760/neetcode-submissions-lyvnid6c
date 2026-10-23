class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = nums[0]

        for i in range(1 , len(nums)):
            if i > maxJump:
                return False
            maxJump = max(maxJump , i + nums[i])
        return True