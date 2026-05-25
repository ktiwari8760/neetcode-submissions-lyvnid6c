class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i , ele in enumerate(nums):
            required = target - ele

            if required in hash:
                return [ hash[required] , i ]
            else:
                hash[ele] = i
        return [-1 , -1]