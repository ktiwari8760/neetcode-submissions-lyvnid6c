class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusting = [0 for _ in range(n+1)]
        trusts = [0 for _ in range(n+1)]

        for a , b in trust:
            trusting[a] += 1
            trusts[b] += 1

        for i in range(1 , n+1):
            if trusting[i] == 0 and trusts[i] == n-1:
                return i
        return -1