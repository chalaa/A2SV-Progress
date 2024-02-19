class Solution:
    def minimumSteps(self, s: str) -> int:
        arr = [i for i in range(len(s)) if s[i]  =='1']
        n = len(s)-1
        ans = 0
        for i in range(len(arr)-1,-1,-1):
            ans += (n-arr[i])
            n-=1
        return ans