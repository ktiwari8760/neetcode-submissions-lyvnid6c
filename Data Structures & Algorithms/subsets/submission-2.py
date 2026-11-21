class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def function(index , arr):
            if index == len(nums):
                answer.append(arr.copy())
                return 
            
            arr.append(nums[index])
            index += 1
            function(index , arr)
            arr.pop()
            function(index , arr)
            return 
        function(0 , [])
        return answer