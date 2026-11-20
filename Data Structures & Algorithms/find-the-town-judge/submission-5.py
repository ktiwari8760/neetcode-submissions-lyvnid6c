class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t = [[] for _ in range(n+1)]

        for ele in trust:
            a , b = ele

            t[b].append(a)
        print(t)
        seen = set()
        for i , ele in enumerate(t):
            print(seen)
            if len(ele) >= n-1 and i not in seen:
                return i
            seen.update(ele)
        return -1
