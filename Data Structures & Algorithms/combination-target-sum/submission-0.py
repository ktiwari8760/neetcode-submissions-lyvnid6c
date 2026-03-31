class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        def helper(start , subset , target):
            if sum(subset) == target:
                answer.append(subset.copy())
            if sum(subset) > target:
                return
            
            for i in range(start , len(nums)):
                subset.append(nums[i])
                helper(i , subset , target)
                subset.pop()
        helper(0 , [] , target)
        return answer