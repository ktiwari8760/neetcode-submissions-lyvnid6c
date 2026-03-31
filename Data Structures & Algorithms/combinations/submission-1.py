class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1 , n+1)]

        answer = []
        def helper(start , subarray):
            if len(subarray) == k:
                answer.append(subarray.copy())
                return 
            if len(subarray) > k:
                return 
            
            for i in range(start , len(arr)):
                subarray.append(arr[i])
                helper(i+1 , subarray)
                subarray.pop()

        helper(0 , [])
        return answer