"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(n , r , c):
            isSame = True
            val = grid[r][c]
            for i in range(n):
                for j in range(n):
                    if grid[r+i][c+j] != val:
                        isSame = False
                        break
            if isSame:
                return Node(val , True)
            
            n = n // 2
            node = Node(0 , False)
            node.topLeft = dfs(n , r , c)
            node.topRight = dfs(n , r , c+n)
            node.bottomLeft = dfs(n , r +n, c)
            node.bottomRight = dfs(n , r+n , c+n)

            return node
        
        return dfs(len(grid) , 0 , 0)