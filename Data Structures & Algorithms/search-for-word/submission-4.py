class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        directions = [[1, 0] , [0, 1] , [-1 , 0] , [0 , -1]]
        def helper(i , j , index):
            if index == len(word):
                return True
            if i < 0 or j < 0 or i >= row or j >= column or (i , j) in seen or board[i][j] != word[index]:
                return False
            seen.add((i , j))
            for dr , dc in directions:
                if helper(i + dr , j + dc , index+1):
                    return True
            seen.remove((i , j))
            return False

        row = len(board)
        column = len(board[0])
        for i in range(row):
            for j in range(column):
                if helper(i , j , 0):
                    return True
        return False