class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')

        def prod ( arr):
            prod = 1
            for i  in range(len(arr)):
                prod = prod * arr[i]
            return prod
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)+1):
                print(nums[i:j])
                product = prod(nums[i:j+1])

                if product > max_prod:
                    max_prod = product
        return max_prod