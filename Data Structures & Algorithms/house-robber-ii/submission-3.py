class Solution:
    def rob(self, nums: List[int]) -> int:
        hash = {}
        if len(nums)==1:
            return nums[0]
        def function(i , end):
            if i > end:
                return 0
            if (i,end) in hash:
                return hash[(i,end)]
            hash[(i,end)] = max((nums[i] + function(i+2 , end)) , function(i+1 , end))
            return hash[(i,end)]
        return max(function(0 , len(nums)-2) , function(1 , len(nums)-1))
