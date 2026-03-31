class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer = []
        in_use = [False] * len(nums)
        def helper(start , subarray):
            if sum(subarray) == target:
                answer.append(subarray.copy())
                return
            if sum(subarray) > target:
                return
            
            for i in range(start , len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subarray.append(nums[i])
                helper(i+1 , subarray)
                subarray.pop()
        helper(0 , [])
        return answer
