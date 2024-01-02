class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        transpose = list(zip(*matrix))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = transpose[i][j]
        for i in range(len(matrix)):
            j = 0
            k = len(matrix[i]) - 1
            while j < k:
                matrix[i][j],matrix[i][k]= matrix[i][k],matrix[i][j]
                j+=1
                k-=1