class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = set()

        for i in range(len(strs)-1):
            mn = min(len(strs[i]),len(strs[i+1]))
            for j in range(mn):
                if strs[i][j] > strs[i+1][j]:
                    ans.add(j)
        return len(ans)

