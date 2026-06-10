class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for ele in nums:
            index = abs(ele)-1
            nums[index] = -1 * abs(nums[index])
        result = []
        for i , ele in enumerate(nums):
            if ele > 0:
                result.append(i+1)
        return result