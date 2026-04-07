class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x // 2
        potential_answer = -1
        while(left <= right):
            mid = (left + right) // 2

            mid_square = mid ** 2

            if mid_square == x:
                return mid
            elif mid_square < x:
                potential_answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return potential_answer