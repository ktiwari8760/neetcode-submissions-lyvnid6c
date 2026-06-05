class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_reach = len(nums)-1

        for i in range(len(nums)-2 , -1 , -1):
            print(i)
            if can_reach <= i + nums[i]:
                can_reach = i
        
        return True if can_reach == 0 else False