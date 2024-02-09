class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row,col = len(matrix), len(matrix[0])
        prefix_sum = [[0]*(col+1) for _ in range(row+1)]
        
        #calculating the prefix_sum for the matrix
        for i in range(row):
            for j in range(col):
                prefix_sum[i+1][j+1] = matrix[i][j] + prefix_sum[i+1][j] + prefix_sum[i][j+1] - prefix_sum[i][j]
        answer = 0

        for r1 in range(1,row+1):
            for r2 in range(r1,row+1):
                #initialize the frequency counter
                freq = defaultdict(int)
                freq[0] += 1
                for c in range(1,col+1):
                    #calculate the current sum for 
                    current_sum = prefix_sum[r2][c] - prefix_sum[r1-1][c]

                    answer += freq[current_sum - target]
                    freq[current_sum] += 1

        return answer