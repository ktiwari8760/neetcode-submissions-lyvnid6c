class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = []
        used = [False] * len(nums)
        nums.sort()
        def helper(start , subarray):
            if len(subarray) == len(nums):
                answer.append(subarray.copy())
            for i in range(0 , len(nums)):
                if used[i]:
                    continue
                # Correct duplicate skip condition
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                subarray.append(nums[i])
                helper(start+1 , subarray)
                used[i] = False
                subarray.pop()

        helper(0 , [])
        return answer
