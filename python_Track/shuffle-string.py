class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [i for i in s]
        for i,v in enumerate(indices):
            ans[v] = s[i]
        return "".join(ans)