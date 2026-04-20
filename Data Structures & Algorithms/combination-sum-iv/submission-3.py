class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {0 : 1}
        def df(total):
            if total == 0:
                return 1
            if total in memo:
                return memo[total]
            
            res = 0
            for i in range(len(nums)):
                if total < nums[i]:
                    break
                res += df(total - nums[i])
            memo[total] = res
            return res
        return df(target)