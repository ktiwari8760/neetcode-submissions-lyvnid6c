class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        half_sum = total // 2
        memo = {}
        
        def df(index, summation):
            if summation == half_sum:
                return True
            if summation > half_sum or index == len(nums):
                return False
            
            if (index, summation) in memo:
                return memo[(index, summation)]
            
            # take
            if df(index + 1, summation + nums[index]):
                memo[(index, summation)] = True
                return True
            
            # not take
            if df(index + 1, summation):
                memo[(index, summation)] = True
                return True
            
            memo[(index, summation)] = False
            return False
        
        return df(0, 0)