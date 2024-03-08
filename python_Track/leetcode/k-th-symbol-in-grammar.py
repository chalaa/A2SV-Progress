class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def rec(n,k,val):
            if n == 1:
                return val
            tot = 2 ** (n-1)

            if k <= tot//2:
                curr_val = 0 if val==0 else 1
                return rec(n-1,k,curr_val)
            else:
                curr_val = 1 if val==0 else 0
                return rec(n-1,k-(tot//2),curr_val)
        return rec(n,k,0)