class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n ==0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        res = self.myPow(x, n // 2)
        res  *= res
        if n % 2:
            res *= x
        return res