class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(piles , rate):
            hours = 0
            for ele in piles:
                hours += math.ceil(ele/rate)
            return hours
        left = min(piles)
        right = max(piles)
        min_rate = float('inf')
        while(left <= right):
            mid = (left + right) //2 
            if helper(piles , mid) <= h:
                min_rate = min(min_rate , mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_rate