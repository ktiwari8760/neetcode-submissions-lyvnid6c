class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_required(weights , capacity):
            day = 0
            single_day_weight = 0
            for ele in weights:
                single_day_weight += ele
                if single_day_weight == capacity:
                    day += 1
                    single_day_weight = 0
                elif single_day_weight > capacity:
                    day += 1
                    single_day_weight = ele
            if single_day_weight > 0:
                day += 1
            return day

        left = max(weights)
        right = sum(weights)
        min_day = float('inf')
        while(left <= right):
            mid = (left+ right) // 2
            if days_required(weights , mid) <= days:
                min_day = min(min_day , mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_day
