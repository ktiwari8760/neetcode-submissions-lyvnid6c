class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i:int , j:int) -> int:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return 0
            if grid[i][j] == 0:
                return 0
            if grid[i][j] < 0:
                return 0
            grid[i][j] = -1
            area = 1
            directions = [[1 , 0] , [-1 , 0] , [0,1] , [0 , -1]]
            for dx , dy in directions:
                area += dfs(i+dx , j + dy)
            return area

        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i , j)
                    max_area = max(max_area , area)
        return max_area