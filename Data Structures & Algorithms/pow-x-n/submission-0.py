class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def function(x  ,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n < 0:
                x = 1/x
                n = -n
            if n % 2 == 0:
                return function(x , n / 2) ** 2
            else:
                return (function(x , (n-1)/2) ** 2 ) * x
        return function(x , n)