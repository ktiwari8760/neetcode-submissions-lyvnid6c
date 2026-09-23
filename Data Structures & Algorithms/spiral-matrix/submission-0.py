class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        top = 0
        while(top <= bottom and left <= right):
            # Travelling Horizontally
            for i in range(left , right+1):
                answer.append(matrix[top][i])
            top += 1
            # Travelling Vertically
            for j in range(top , bottom+1):
                answer.append(matrix[j][right])
            right -= 1
            # travelling Bottom
            if top <= bottom:
                for i in range(right , left-1 , -1):
                    answer.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    answer.append(matrix[i][left])
                left += 1
        return answer
