class Solution:
    def tribonacci(self, n: int) -> int:
        hash = {}
        def func(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 1
            if i < 0:
                return 0
            if i in hash.keys():
                return hash[i]
            hash[i] = func(i-1) + func(i-2) + func(i-3)
            return hash[i]
        return func(n)