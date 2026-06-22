class Node:
    def __init__(self  ,val , neighbours):
        self.val = val
        self.neighbours = neighbours
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash = {}

        for ele in prerequisites:
            a , b = ele
            if a in hash:
                hash[a].neighbours.append(b)
            else:
                newNode = Node(a , [b])
                hash[a] = newNode
        
        def dfs(node , seen):
            if not node:
                return True
            if node in seen:
                return False
            seen.add(node)
            for n in node.neighbours:
                if not dfs(hash.get(n) , seen):
                    return False
            seen.remove(node)
            return True
        for key in hash.keys():
            if not dfs(hash[key] , set()):
                return False
        return True
