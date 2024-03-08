class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dict = {intervals[i][0]: i for i in range(len(intervals))}
        arr = sorted(dict.keys())
        ans = [-1] * len(intervals)
        for start,end in intervals:
            ind = bisect_left(arr,end)
            if ind != len(arr):
                ans[dict[start]] = dict[arr[ind]]
        return ans