class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def addRoom(i , j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == -1 or (i , j) in visited:
                return
            visited.add((i , j))
            q.append((i , j))
        q = deque([])
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i , j))
                    visited.add((i , j))
        length = len(q)
        distance = 0
        while q:
            for i in range(len(q)):
                r , c = q.popleft()
                grid[r][c] = distance
                distances = [[1 , 0] , [-1 , 0] , [0 , 1] , [0,-1]]
                for dr , dc in distances:
                    addRoom(r+dr , c+dc)
            distance += 1


        