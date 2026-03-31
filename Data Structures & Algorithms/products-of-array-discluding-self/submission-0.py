class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        arr = [1] * len(nums)
        for i , ele in enumerate(nums):
            arr[i] = product
            product = product * nums[i]
        print(arr)
        product = 1
        for i in range(len(nums)-1 , -1 , -1):
            arr[i] *= product
            product = product * nums[i]
        return arr