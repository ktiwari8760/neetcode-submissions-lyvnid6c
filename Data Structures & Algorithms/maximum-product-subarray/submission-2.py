class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        min_prod = float('inf')
        prod = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                prod = 1
                continue
            prod = prod * nums[i]
            print(prod , max_prod)
            max_prod = max(prod , max_prod , nums[i])
            min_prod = min(prod , min_prod  , nums[i])
        return max_prod 