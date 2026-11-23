class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue
                if (i in row.keys() and val in row[i]) or (j in col.keys() and val in col[j]) or ((i//3 , j//3) in box.keys() and val in box[(i // 3 , j //3)]):
                    return False
                
                row[i] = row.get(i , []) + [val]
                col[j] = col.get(j , []) + [val]
                box[(i//3 , j//3)] = box.get((i//3 , j//3) , [])  + [val]
        return True