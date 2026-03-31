class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        def helper(start , subset , total):
            if total == target:
                answer.append(subset.copy())
                return
            if start >= len(nums) or total > target:
                return
            
            subset.append(nums[start])
            helper(start , subset , total + nums[start])
            subset.pop()
            helper(start+1 , subset , total)
        helper(0 , [] , 0)
        return answer