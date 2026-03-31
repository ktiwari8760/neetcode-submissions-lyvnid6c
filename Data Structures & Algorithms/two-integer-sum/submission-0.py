class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in dict1.keys():
                return[dict1[temp] , i]
            dict1[nums[i]] = i
        return [-1,-1]
        