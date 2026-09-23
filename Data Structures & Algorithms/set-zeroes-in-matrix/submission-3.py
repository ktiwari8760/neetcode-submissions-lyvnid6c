class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    # marking rows
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = -1
                    for m in range(len(matrix)):
                        if matrix[m][j] != 0:
                            matrix[m][j] = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
