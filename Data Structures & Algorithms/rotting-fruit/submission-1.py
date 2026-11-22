class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Insert all the rotted oranges in a q
        q = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i , j))
        seconds = 0
        while q:
            length = len(q)
            flag = False
            for _ in range(length):
                i , j = q.popleft()
                directions = [[1 , 0] , [-1 , 0] , [0 , 1] , [0,-1] ]
                for dx , dy in directions:
                    x = dx + i
                    y = dy + j
                    if (x in range(0 , len(grid))) and (y in range(0 , len(grid[0]))) and (grid[x][y] == 1):
                        flag = True
                        q.append((x , y))
                        grid[x][y] = 2
            if flag:
                seconds += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return  seconds