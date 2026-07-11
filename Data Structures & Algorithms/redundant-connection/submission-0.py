class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        print(parent)
        rank = [1 for _ in range(len(edges)+1)]

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node
        
        def union(n1 , n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            if rank[p2] > rank[p1]:
                p1 , p2 = p2 , p1
            parent[p2] = p1
            rank[p2] += rank[p1]
            return True
        
        for u , v in edges:
            if not union(u , v):
                return [u , v]
        return []