class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        def recursion(index , subarr):
            if sum(subarr) == target:
                answer.append(subarr.copy())
                return
            if sum(subarr) > target:
                return
            for i in range(index , len(nums)):
                subarr.append(nums[i])
                recursion(i , subarr)
                subarr.pop()
        recursion(0 , [])
        return answer