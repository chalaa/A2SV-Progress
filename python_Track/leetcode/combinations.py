class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(arr,j):
            nonlocal ans
            if len(arr) == k:
                ans.append(arr.copy())
                return
            for i in range(j,n+1):
                arr.append(i)
                backtrack(arr,i+1)
                arr.pop()
        backtrack([],1)
        return ans
