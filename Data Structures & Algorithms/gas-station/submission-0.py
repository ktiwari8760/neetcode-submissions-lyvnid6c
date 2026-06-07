class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            gas_in_car = 0
            for k in range(i , i+ n):
                k = k % n
                gas_in_car = (gas_in_car + gas[k]) - cost[k]
                if gas_in_car < 0:
                    break
            if gas_in_car >= 0:
                return i
        return -1
