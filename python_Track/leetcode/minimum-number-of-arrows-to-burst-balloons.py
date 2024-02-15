class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        points.sort(key = lambda x : x[1])
        min_end = points[0][1]
        for i in range(len(points)):
            if points[i][0] > min_end:
                ans += 1
                min_end = points[i][1]
        return ans
        