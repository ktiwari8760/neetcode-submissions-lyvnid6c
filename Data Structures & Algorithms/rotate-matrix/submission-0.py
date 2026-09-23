class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Rotating a matrix 
        # Step 1 reverse matrix vertically
        left = 0
        right = len(matrix)-1
        while(left<=right):
            matrix[left] , matrix[right] = matrix[right] , matrix[left]
            left += 1
            right -= 1
        
        # We take the transpose of the matrix row becomes column and column becomes row

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i <= j:
                    matrix[i][j] , matrix[j][i] = matrix[j][i] ,  matrix[i][j]
        return None
