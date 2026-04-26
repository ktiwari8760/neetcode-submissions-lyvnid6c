class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i , ele in enumerate(nums):
            diff = target-ele
            if diff in map:
                return [map[diff] ,i ]
            map[ele] = i
        
        return [-1 , -1]