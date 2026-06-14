class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i , j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] == "0":
                return 0
            if grid[i][j] == "-1":
                return 0
            grid[i][j] = "-1"
            directions = [[1 , 0] , [-1 , 0] , [0 , 1] , [0,-1]]
            # Explore paths
            for dx , dy in directions:
                dfs(i+dx , j+dy)
            return 1

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    counter += dfs(i , j)
        return counter