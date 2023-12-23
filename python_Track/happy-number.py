class Solution:
    def isHappy(self, n: int) -> bool:
        if n <10 :
            n = n**2
        st = str(n)
        while len(st)>1:
            ans = 0
            for i in st:
                ans += int(i)**2
            st = str(ans)
        if st == '1' or st == '7':
            return True
        return False