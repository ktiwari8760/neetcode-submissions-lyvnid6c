class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def helper(mid , weights):
            days = 0
            single_day_weight = 0
            for ele in weights:
                single_day_weight += ele
                if single_day_weight == mid:
                    days += 1
                    single_day_weight = 0
                elif single_day_weight > mid:
                    days += 1
                    single_day_weight = ele
            if single_day_weight > 0:
                days += 1
            return days


        left = max(weights)
        right = sum(weights)
        min_days = float('inf')
        while(left<=right):
            mid = (left+right)//2

            if helper(mid , weights) <= days:
                min_days = min(mid , min_days)
                right = mid-1
            else:
                left = mid+1
        return min_days