class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        answer = []
        def helper(start , subset):
            if sum(subset) == target:
                answer.append(subset.copy())
                return
            if sum(subset) > target:
                return
            for i in range(start , len(nums)):
                subset.append(nums[i])
                helper(i , subset)
                subset.pop()
        helper(0 , [])
        return answer