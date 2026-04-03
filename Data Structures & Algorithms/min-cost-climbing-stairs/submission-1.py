class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        hashmap = {}
        def helper(index , path_cost):
            if index >= len(cost):
                return path_cost
            if (index , path_cost) in hashmap.keys():
                return hashmap[(index , path_cost)]
            hashmap[(index , path_cost)] = min(helper(index + 1 , path_cost + cost[index]) , helper(index+2 , cost[index] + path_cost))
            return hashmap[(index , path_cost)]
        return min(helper(0 , 0) , helper(1 , 0))