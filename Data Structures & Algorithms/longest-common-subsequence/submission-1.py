class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memoisation = [[-1] * len(text2) for _ in range(len(text1))]
        def solve(i , j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if memoisation[i][j] != -1:
                return memoisation[i][j]
            if text1[i] == text2[j]:
                memoisation[i][j] = 1 + solve(i + 1 , j+1)
                return memoisation[i][j]
            memoisation[i][j] = max(solve(i+1 , j) , solve(i , j+1))
            return memoisation[i][j]
        return solve(0 , 0)