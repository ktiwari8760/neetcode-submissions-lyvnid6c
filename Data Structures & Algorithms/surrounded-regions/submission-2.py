class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        def dfs(i , j):
            if i not in range(ROWS) or j not in range(COLS):
                return 
            if (i , j) in visited:
                return 
            if board[i][j] == 'X':
                return
            visited.add((i , j))
            directions = [[0,1] , [1 , 0] , [0 , -1] , [-1 , 0]]
            board[i][j] = 'T'
            for dx , dy in directions:
                dfs(i  + dx , j+dy )
            return
        
        for i in range(ROWS):
            dfs(i , 0)
            dfs(i , COLS-1)
        for j in range(COLS):
            dfs(0,j)
            dfs(ROWS-1 , j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
