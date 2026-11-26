class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        left = 1
        right = max(nums)+2
        hash = set(nums)
        flag = False
        for ele in nums:
            if ele > 0:
                flag = True
                break
        if not flag:
            return 1
        for i in range(left , right):
            if i not in hash:
                return i
        return -1