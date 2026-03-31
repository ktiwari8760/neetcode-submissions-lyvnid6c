class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    
        answer = []
        candidates.sort()
        def helper(start , subset , sum_):
            if sum_ == target:
                answer.append(subset.copy())
                return
            if sum_ > target:
                return
            
            for i in range(start , len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                subset.append(candidates[i])
                helper(i+1 , subset , sum_+candidates[i])
                subset.pop()
        helper(0 , [] , 0)
        return answer