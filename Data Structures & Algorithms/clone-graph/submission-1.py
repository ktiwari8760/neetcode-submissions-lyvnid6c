"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hash = {}
        def dfs(node):
            if not node:
                return None
            if node in hash:
                return hash[node]
            newNode = Node(node.val)
            hash[node] = newNode
            for neighbor in node.neighbors:
                clone = dfs(neighbor)
                newNode.neighbors.append(clone if clone else None)
            return newNode
        return dfs(node)