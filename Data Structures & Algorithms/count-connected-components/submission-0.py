class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbours = {i : [] for i in range(n)}
        print(neighbours)

        for u , v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)
        visited = [False for _ in range(n)]
        def dfs(n):
            if visited[n]:
                return 0
            visited[n] = True
            for neig in neighbours[n]:
                dfs(neig)
            return 1
        
        counter = 0
        for i in range(n):
            counter += dfs(i)
        return counter
