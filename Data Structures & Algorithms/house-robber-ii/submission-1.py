class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def func(start , end):
            hash = {}
            def helper(n):
                if n > end:
                    return 0
                if n < start:
                    return 0
                if n in hash.keys():
                    return hash[n]
                hash[n] = max(helper(n-1) , (helper(n-2) + nums[n]))
                return hash[n]
            return helper(end)
        return max(func(0 , len(nums)-2) , func(1 , len(nums)-1))
        