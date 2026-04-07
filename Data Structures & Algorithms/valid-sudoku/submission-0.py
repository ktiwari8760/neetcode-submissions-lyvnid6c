class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = defaultdict(set)
        col_hash = defaultdict(set)
        matrix_hash = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # They are empty place holders
                    continue
                if board[r][c] in row_hash[r] or board[r][c] in col_hash[c] or board[r][c] in matrix_hash[(r//3 , c//3)]:
                    return False
                row_hash[r].add(board[r][c])
                col_hash[c].add(board[r][c])
                matrix_hash[(r//3 , c//3)].add(board[r][c])
        return True