class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        lst = []
        for item in ranges:
            inlst = [i for i in range(item[0], item[1] +1)]
            lst+=inlst
        for i in range(left, right+1):
            if i not in lst:
                return False
        return True