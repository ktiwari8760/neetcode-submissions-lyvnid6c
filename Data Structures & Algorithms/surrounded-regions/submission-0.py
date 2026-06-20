class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COL = len(board[0])
        def dfs(r , c):
            if r < 0 or c < 0 or r == ROWS or c == COL or board[r][c] != "O":
                return
            board[r][c] = "T"
            directions = [[1 , 0] , [-1 , 0] , [0 , 1] , [0 , -1]]
            for dr , dc in directions:
                dfs(r+dr , c+dc)
        
        # We check for the borders
        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r , 0)
            if board[r][COL-1] == "O":
                dfs(r , COL-1)
        
        for c in range(COL):
            if board[0][c] == "O":
                dfs( 0 , c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1 , c)
        
        for i in range(ROWS):
            for j in range(COL):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        
        
                