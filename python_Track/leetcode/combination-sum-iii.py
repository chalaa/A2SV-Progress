class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        arr = []
        can = [i+1 for i in range(min(n,9))]
        def backtrack(ind,_sum):
            if k == len(arr):
                if _sum == n:
                    ans.append(arr[:])
                return
            if _sum > n:
                return
            for i in range(ind,len(can)):
                arr.append(can[i])
                _sum += can[i]
                backtrack(i+1,_sum)
                _sum -= can[i]
                arr.pop()  
        backtrack(0,0)
        return ans    