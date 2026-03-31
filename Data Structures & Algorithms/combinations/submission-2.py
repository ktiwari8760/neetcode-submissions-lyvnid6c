class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def helper(start , subset):
            if len(subset) == k:
                answer.append(subset.copy())
            
            for i in range(start , n+1):
                subset.append(i)
                helper(i+1 , subset)
                subset.pop()
        
        helper(1 , [])
        return answer