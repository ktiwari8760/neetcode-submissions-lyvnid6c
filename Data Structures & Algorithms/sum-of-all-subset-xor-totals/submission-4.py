class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum = 0
        def function(index , xor):
            nonlocal sum
            if index == len(nums):
                sum += xor
                return
            
            function(index + 1 , xor ^ nums[index])
            function(index + 1 , xor)
            return 
        function(0 , 0)
        return sum