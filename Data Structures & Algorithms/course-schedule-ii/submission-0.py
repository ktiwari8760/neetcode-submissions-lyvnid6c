class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = {c : [] for c in range(numCourses)}
        for a , b in prerequisites:
            preq[a].append(b)
        output = []
        visit , cycle = set() , set()

        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for pre in preq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
        
