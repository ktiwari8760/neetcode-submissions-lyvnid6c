class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer = []

        def helper(start , subset , sum_):
            if sum_ == target:
                answer.append(subset.copy())
                return
            if start >= len(nums) or sum_ > target:
                return
            
            for i in range(start , len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                helper(i+1 , subset , sum_+nums[i])
                subset.pop()
        helper(0 , [] , 0)
        return answer