class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        used = [False] * len(nums)

        def helper(subset):
            if len(subset) == len(nums):
                answer.append(subset.copy())
                return
            
            for i in range(0 , len(nums)):
                if used[i] == True:
                    continue
                used[i] = True
                subset.append(nums[i])
                helper(subset)
                subset.pop()
                used[i] = False

        helper([])
        return answer
        