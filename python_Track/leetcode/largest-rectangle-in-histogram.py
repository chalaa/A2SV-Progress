class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        _max = 0
        n = len(heights)
        for i in range(len(heights)):
            ind = i
            while stack and stack[-1][0] > heights[i]:
                x = stack.pop()
                ind = x[1]
                _max = max(_max,(i - x[1])*x[0])
            stack.append((heights[i],ind))

        while stack:
            x = stack.pop()
            _max = max(_max,(n - x[1])*x[0])
        return _max