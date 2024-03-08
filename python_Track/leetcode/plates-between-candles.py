class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        arr = []
        ans = []
        prefix = [0]
        for i in range(len(s)):
            if s[i] == '|':
                arr.append(i)
                prefix.append(0)
            else:
                prefix.append(1)
        _sum = list(accumulate(prefix))
        for l,r in queries:
            if l==r:
                ans.append(0)
                continue
            i = bisect_left(arr,l)
            if i < len(arr):
                i = arr[i]
                j = arr[bisect_right(arr,r) - 1]
                if i > r:
                    ans.append(0)
                else:
                    ans.append(_sum[j]-_sum[i])
            else:
                ans.append(0)
        return ans