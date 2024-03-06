class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            mid = l + (r-l)//2
            k = 0
            for i in piles:
                k += ceil(i/mid)
            if k > h:
                l = mid+1
            else:
                r = mid-1
        return l