class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = [max(i) for i in grid]
        cols = [max(i) for i in list((zip(*grid)))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                x = min(rows[i],cols[j])
                ans += (x - grid[i][j])
        
        return ans