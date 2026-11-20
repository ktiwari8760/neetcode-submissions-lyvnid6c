class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def function(i , j):
            if (i not in range(0 , len(grid))) or (j not in range(0 , len(grid[0]))):
                return 1
            if (i , j) in visited:
                return 0
            if grid[i][j] == 0:
                return 1
            
            visited.add((i , j))
            perimeter = 0
            directions = [[1,0] , [-1 , 0] , [0 , 1] , [0,-1]]
            for dx , dy in directions:
                perimeter += function(i+dx , j+dy)
            return perimeter
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += function(i , j)
        return perimeter
