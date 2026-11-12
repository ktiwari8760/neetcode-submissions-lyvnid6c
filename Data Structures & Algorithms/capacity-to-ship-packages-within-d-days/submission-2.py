class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_ship(capacity):
            day = 1
            cap = 0
            for ele in weights:
                if cap+ele > capacity:
                    day += 1
                    cap = 0
                cap += ele
            return day <= days
            

        left = max(weights)
        right = sum(weights)
        answer = float('inf')
        while(left <= right):
            mid = (left + right) //2

            if can_ship(mid):
                answer = min(answer , mid)
                right = mid-1
            else:
                left = mid+1
        return answer
