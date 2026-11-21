from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        q = deque()

        # Start from every treasure chest
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == INF:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni, nj))