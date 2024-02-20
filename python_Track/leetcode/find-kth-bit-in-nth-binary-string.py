class Solution:
    def invert(self,s):
        for i in range(len(s)):
            if s[i] =='0':
                s[i] = '1'
            else:
                s[i] = '0'
        return "".join(s)
    def generate(self,n):
        if n == 0:
            return '0'
        temp = self.generate(n-1)
        return temp + '1' + self.invert(list(temp))[::-1]
    def findKthBit(self, n: int, k: int) -> str:
        return self.generate(n-1)[k-1]