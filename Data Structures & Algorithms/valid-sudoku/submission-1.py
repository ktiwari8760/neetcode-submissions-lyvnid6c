class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}

        def check_sudoku(r , c):
            if board[r][c] == ".":
                return True
            if board[r][c] in row.get(r , set()) or board[r][c] in col.get(c , set()) or board[r][c] in box.get((r // 3, c // 3) , set()):
                return False
            row.setdefault(r, set()).add(board[r][c])
            col.setdefault(c, set()).add(board[r][c])
            box.setdefault((r // 3, c // 3), set()).add(board[r][c])
            return True
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                    if not check_sudoku(i , j):
                        return False
        return True