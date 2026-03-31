class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 # Initialised a result

        for i in range(32):
            bit = (n >> i) & 1 # This will tell my bit is 1 or 0

            res = res | (bit << (31-i))

        return res