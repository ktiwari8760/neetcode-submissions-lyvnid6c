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
        def function(node):
            if not node:
                return None
            if node in hash:
                return hash[node]
            newNode = Node(node.val)
            hash[node] = newNode
            for n in node.neighbors:
                newNode.neighbors.append(function(n))
            return newNode
        return function(node)