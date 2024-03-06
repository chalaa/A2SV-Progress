# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i = 1
        while i <= n:
            mid = i+(n-i)//2
            if isBadVersion(mid):
                n = mid - 1
            else:
                i = mid+1
        return i
        