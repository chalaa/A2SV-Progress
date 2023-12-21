class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        pr = int(n**(1.0/3))
        while pr>=0 and n>=0:
            if n >= 3**pr:
                n-= 3**pr
            pr-=1
        if n==0:
            return True
        return False
            