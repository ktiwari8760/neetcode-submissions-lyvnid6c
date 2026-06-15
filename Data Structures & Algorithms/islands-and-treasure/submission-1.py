class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows , cols = len(grid) , len(grid[0])
        INF = 2147483647
        visit = [[False for _ in range(cols)] for _ in range(rows)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(i , j):
            queue = deque([(i , j)])
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            visited[i][j] = True
            steps = 0
            while queue:
                for _ in range(len(queue)):
                    row , col = queue.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr , dc in directions:
                        nr , nc = dr + row , dc+col
                        if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] != -1:
                            visited[nr][nc] = True
                            queue.append((nr , nc))
                steps += 1
            return INF
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2147483647:
                    grid[i][j] = bfs(i , j)
        return None

            