class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ls=['a', 'e', 'i', 'o','u']
        ct=0
        for i in range(k):
            if s[i] in ls:
                ct+=1
        i=0
        j=k
        mx=max(0,ct)
        while j<len(s):
            if s[j] in ls and s[i] in ls:
                j+=1
                i+=1
            elif s[j] in ls:
                ct+=1
                j+=1
                i+=1
            elif s[i] in ls:
                ct-=1
                j+=1
                i+=1
            else:
                j+=1
                i+=1
            mx=max(mx,ct)
        return mx
            
