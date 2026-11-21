class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def function(i , j):
            if i not in range(0 , len(grid)) or j not in range(0 , len(grid[0])):
                return 0
            if (i , j) in visited:
                return 0
            if grid[i][j] == 0:
                return 0
            visited.add((i , j))
            area = 1

            directions = [[1 , 0] , [-1 , 0] , [0,1] , [0,-1]]

            for dx , dy in directions:
                area += function(i+dx , j+dy)
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = function(i , j)
                    max_area = max(max_area , area)
        return max_area