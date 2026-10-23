class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        right = 0
        jump = 0
        while (left < len(nums)-1 and right < len(nums)-1):
            maxJumpPossible = 0

            for i in range(left , right+1):
                maxJumpPossible = max(maxJumpPossible , nums[i] + i)
            
            left = right
            right = maxJumpPossible
            jump += 1
        
        return jump