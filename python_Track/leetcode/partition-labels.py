class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ## precomputing the last indicies of each character
        d = {}
        for i in range(len(s)-1,-1,-1):
            if s[i] not in d:
                d[s[i]] = i
        _min = 0
        _max = 0
        res = []
        for i in range(len(s)):
            if _max < d[s[i]]:
                _max = d[s[i]]
            if i == _max:
                res.append(_max-_min+1)
                _min = i+1
        return res