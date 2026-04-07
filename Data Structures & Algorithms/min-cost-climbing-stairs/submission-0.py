class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def helper(index , path_cost):
            if index >= len(cost):
                return path_cost
            return min(helper(index + 1 , path_cost + cost[index]) , helper(index+2 , cost[index] + path_cost))
        return min(helper(0 , 0) , helper(1 , 0))