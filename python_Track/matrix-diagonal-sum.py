class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = 0
        j=n-1
        for i in range(n):
            ans += mat[i][i]
            if i != j:
                ans += mat[j][i]
            j-=1
        return ans
        