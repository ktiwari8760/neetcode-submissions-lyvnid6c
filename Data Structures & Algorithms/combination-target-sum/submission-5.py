class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        def recursion(index , subarr , sum_):
            if sum_ == target:
                answer.append(subarr.copy())
                return
            if sum_ > target:
                return
            for i in range(index , len(nums)):
                subarr.append(nums[i])
                sum_ += nums[i]
                recursion(i , subarr , sum_)
                sum_ -= nums[i]
                subarr.pop()
        recursion(0 , [] , 0)
        return answer