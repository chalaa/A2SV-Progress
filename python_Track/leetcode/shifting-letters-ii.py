class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        dic = dict(zip(string.ascii_lowercase, range(0,26)))
        rev_dic = {v:k for k,v in dic.items()}
        d = [0 for _ in range(len(s) + 1)]
        for start, end, direction in shifts:
            dir = 1 if direction else -1
            d[start] += dir
            d[end + 1] -= dir
        ans=""
        for i in range(len(s)):
            if i != 0: 
                d[i] += d[i - 1]
            ans+=rev_dic[(dic[s[i]] + d[i]) %26]
        return ans

        