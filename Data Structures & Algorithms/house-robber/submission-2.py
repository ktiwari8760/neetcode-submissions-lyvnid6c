class Solution:
    def rob(self, nums: List[int]) -> int:
        hash = {}
        def function(i):
            if i > len(nums)-1:
                return 0
            if i in hash:
                return hash[i]
            hash[i] = max((nums[i] + function(i+2)) , function(i+1))
            return hash[i]
        return function(0)
