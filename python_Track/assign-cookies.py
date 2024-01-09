class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        ct = 0
        i,j = len(s)-1, len(g)-1
        while i > -1 and j > -1:
            if g[j] <= s[i]:
                ct += 1
                i -= 1
                j -= 1
            else:
                j -= 1
        return ct
        