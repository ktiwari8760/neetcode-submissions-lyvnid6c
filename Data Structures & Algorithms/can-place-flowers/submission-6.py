class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        if len(f) == 1:
            if f[0] == 0:
                n = n-1
        if len(f) >= 2:
            if f[0] == 0 and f[1] != 1:
                n = n-1
            if f[-1] == 0 and f[-2] != 1:
                n = n-1
        for i in range(1 , len(f)-1):
            if f[i] == 0 and f[i-1] != 1 and f[i+1] != 1:
                f[i] = 1
                n = n-1
        return n <= 0
                