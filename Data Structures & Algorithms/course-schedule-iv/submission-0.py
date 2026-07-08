class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for preq , crs in prerequisites:
            adj[crs].append(preq)
        
        def dfs(crs):
            if crs not in pre_hash:
                pre_hash[crs] = set()

                for pre in adj[crs]:
                    pre_hash[crs] |= dfs(pre)
                pre_hash[crs].add(crs)
            return pre_hash[crs]
        
        pre_hash = {}
        for crs in range(numCourses):
            dfs(crs)
        res = []
        for u , v in queries:
            res.append(u in pre_hash[v])
        return res
        