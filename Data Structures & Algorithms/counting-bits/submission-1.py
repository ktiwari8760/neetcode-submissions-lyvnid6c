class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1

        for ele in range(1 , n+1):
            if offset * 2 == ele:
                # We reached the double now update
                offset = ele
            dp[ele] = 1 + dp[ele-offset]
        
        return dp