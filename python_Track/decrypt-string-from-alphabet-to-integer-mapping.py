class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = {i:chr(i+96) for i in range(1,27)}
        i=0
        ans = ""
        while i < len(s) -2:
            if s[i+2].isnumeric():
                ans += dic[int(s[i])]
                i+=1
            else:
                j = s[i:i+2]
                ans += dic[int(s[i:i+2])]
                i+=3
        while i< len(s):
            ans += dic[int(s[i])]
            i+=1
        return ans