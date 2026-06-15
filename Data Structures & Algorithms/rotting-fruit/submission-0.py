class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque()
        time =0 
        directions = [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rotten.append((i , j))
        
        while fresh > 0 and rotten:
            length = len(rotten)

            for _ in range(length):
                r  ,c  = rotten.popleft()
                for dr , dc in directions:
                    nr , nc = r + dr , c + dc

                    if (nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1):
                        fresh -= 1
                        rotten.append((nr , nc))
                        grid[nr][nc] = 2
            time += 1
        return time if fresh == 0 else -1