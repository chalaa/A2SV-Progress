class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i < len(matrix)-1 and j < len(matrix[i])-1:
                    if matrix[i+1][j+1] != matrix[i][j]:
                        return False
        return True
        