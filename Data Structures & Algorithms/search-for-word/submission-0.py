class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        hashset = set()

        def helper(index , row , column ):
            if index == len(word):
                return True
            if (row < 0 or
                column < 0 or
                row >= len(board) or 
                column >= len(board[0]) or 
                (row , column) in hashset or
                board[row][column] != word[index]):
                return False
            
            hashset.add((row , column))
            result = (helper(index+1 , row+1 , column) or
            helper(index+1 , row , column+1) or
            helper(index+1 , row-1 , column) or 
            helper(index+1 , row , column-1)  )

            hashset.remove((row , column))

            return result
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(0 , i , j):
                    return True
        return False

