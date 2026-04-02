class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap = {}
        def function(n):
            if n == 0:
                return 1
            if n == 1:
                return 1
            if n in hashmap.keys():
                return hashmap[n]
            hashmap[n] = function(n-1) + function(n-2)
            return hashmap[n]
        return function(n)