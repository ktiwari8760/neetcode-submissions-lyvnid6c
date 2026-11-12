class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat(speed) -> int:
            """Returns the hours taken to eat bananas"""
            time = 0
            for p in piles:
                time += math.ceil(p / speed)
            return time <= h

        left = 1
        right = max(piles)

        if h < len(piles):
            return -1
        answer = float('inf')
        while(left<= right):
            mid = (left+right) // 2
            if can_eat(mid):
                answer = min(answer , mid)
                right = mid-1
            else:
                left = mid+1
        return answer

