class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        product = 1
        for i , ele in enumerate(nums):
            arr[i] = product
            product = product * ele
        product = 1
        for i  in range(len(nums)-1 , -1 , -1):
            ele = nums[i]
            arr[i] = arr[i] * product
            product = product * ele
        return arr
