class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0

        def helper(start , subarray):
            nonlocal result             
            xor = 0
            for ele in subarray:
                xor = xor^ele
            result += xor
            
            for i in range(start , len(nums)):
                subarray.append(nums[i])
                helper(i+1 , subarray)
                subarray.pop()
        helper(0 , [])
        return result
