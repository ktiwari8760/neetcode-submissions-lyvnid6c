class Solution:
    def climbStairs(self, n: int) -> int:
        def function(n):
            if n == 0:
                return 1
            if n == 1:
                return 1
            return function(n-1) + function(n-2)
        return function(n)