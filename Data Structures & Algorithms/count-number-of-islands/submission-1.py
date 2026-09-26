class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0] , [0,1] , [-1 , 0] , [0,-1]]
        def dfs(i , j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] != "1":
                return 
            grid[i][j] = -1
            for dr , dc in directions:
                dfs(dr+i , dc+j)
            return 
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i , j)
                    counter += 1
        return counter