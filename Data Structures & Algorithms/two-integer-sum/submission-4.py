class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i , ele in enumerate(nums):
            diff = target - ele
            if diff in hash.keys():
                return [hash[diff] , i]
            hash[ele] = i
        return [-1 , -1]