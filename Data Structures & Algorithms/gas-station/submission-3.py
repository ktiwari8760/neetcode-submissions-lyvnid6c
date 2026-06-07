class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total_gas = 0
        index = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            if total_gas < 0:
                total_gas = 0
                index =i+ 1
        return index
