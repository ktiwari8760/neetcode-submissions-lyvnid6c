class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows , cols = len(matrix) , len(matrix[0])
        self.sumMat = [[0 for _ in range(cols+1)] for _ in range(rows+1)]

        for i in range(rows):
            sum = 0
            for j in range(cols):
                sum += matrix[i][j]
                above = self.sumMat[i][j+1]
                self.sumMat[i+1][j+1] = sum + above
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        topLeft = self.sumMat[row1 - 1][col1 - 1]
        return bottomRight - above - left + topLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)