class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        i=0
        if n>=7:
            j=7
        else:
            return n*(n+1)//2
        while n > 0:
            x=j*(j+1)//2
            y=i*(i+1)//2
            ans+=(x-y)
            i+=1
            n -= 7
            if n>=7:
                j+=1
            else:
                j = n+i
        return ans

        