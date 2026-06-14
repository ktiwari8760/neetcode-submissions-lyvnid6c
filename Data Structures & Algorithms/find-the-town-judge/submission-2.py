class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [[] for _ in range(n)]

        for i in range(len(trust)):
            trusted[trust[i][0]-1].append(trust[i][1])
        index = []
        for idx , t in enumerate(trusted):
            if not t:
                index.append(idx+1)
        print(index)
        if len(index) != 1:
            return -1
        for idx ,  t in enumerate(trusted):
            if idx != index[0] - 1 and  index[0] not in t:
                return -1
        return index[0]
