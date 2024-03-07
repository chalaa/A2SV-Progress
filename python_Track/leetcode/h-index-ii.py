class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) -1
        n = len(citations)
        best = 0
        while left <= right:
            mid = left + (right-left)//2
            if citations[mid] < (n-mid):
                left = mid + 1
            else:
                best = max(best,n-mid)
                right = mid-1
        return best
