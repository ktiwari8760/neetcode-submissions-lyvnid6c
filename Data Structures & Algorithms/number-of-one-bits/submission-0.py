class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        for i in range(0 , 32):
            mask = 1 << i
            is_set = mask & n

            if is_set != 0:
                res += 1
            else:
                continue
        return res