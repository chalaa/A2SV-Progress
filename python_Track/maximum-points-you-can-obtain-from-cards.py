class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        _sum = _max = sum(cardPoints[:k])
        i = k-1
        j = len(cardPoints)-1
        while i >= 0:
            _sum -= cardPoints[i]
            _sum += cardPoints[j]
            _max = max(_max,_sum)
            i -= 1
            j -= 1
        return _max
