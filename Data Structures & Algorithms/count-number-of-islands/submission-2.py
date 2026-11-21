class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def function(i  ,j):
            if i  not in range(0 , len(grid)) or j not in range(len(grid[0])):
                return False
            if grid[i][j] == "0":
                return False
            if (i , j) in visited:
                return False
            visited.add((i , j))

            directions = [[1 , 0] , [0 , -1],[0 , 1] , [-1 , 0]]

            for dx , dy in directions:
                function(i + dx , j + dy)
            return True
        island = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    if function(i , j):
                        island += 1
        return island
