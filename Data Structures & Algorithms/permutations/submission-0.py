class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        used = [False] * len(nums)
        def helper(start , subarray):
            if len(subarray) == len(nums):
                answer.append(subarray.copy())
                return
            
            for i in range(0 , len(nums)):
                if used[i]:
                    continue
                used[i] = True
                subarray.append(nums[i])
                helper(i+1 , subarray)
                subarray.pop()
                used[i] = False
        helper(0 , [])
        return answer