class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        hash = {}
        def backtracking(index , sum_):
            if index == len(nums):
                return 1 if sum_ == target else  0
            if (index , sum_) in hash:
                return hash[(index , sum_)]
            hash[(index , sum_)] = backtracking(index +1 , sum_ + nums[index]) + backtracking(index + 1 , sum_ - nums[index])
            return hash[(index , sum_)]
        
        return backtracking(0 , 0)
