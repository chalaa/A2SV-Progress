class Solution:
    def sortSentence(self, s: str) -> str:
        strings = s.split()
        ans = [""] * 10
        for i in strings:
            x = int(i[-1])
            ans[x] = i[:-1]
        return " ".join(ans).strip()
