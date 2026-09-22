class Solution:
    def climbStairs(self, n: int) -> int:
        # Number of ways to climb 
        hash = {}
        def function(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in hash:
                return hash[n]
            hash[n] = function(n-1) + function(n-2)
            return hash[n]
        return function(n)