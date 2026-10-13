class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        current_step_max = nums[0]
        max_can_go = nums[0]
        jump = 1
        for i in range(1 , len(nums)):
            if i > current_step_max and i <= max_can_go:
                current_step_max = max_can_go
                max_can_go = max(max_can_go , nums[i] + i)
                jump += 1
            else:
                max_can_go = max(max_can_go , nums[i] + i)
    
        return jump