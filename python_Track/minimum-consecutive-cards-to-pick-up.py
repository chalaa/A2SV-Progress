class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        _min = float('inf')
        _set = set()
        i = 0
        j = 0
        while j < len(cards):
            while cards[j] in _set:
                _set.remove(cards[i])
                _min = min(_min,j-i)
                i += 1
            _set.add(cards[j])
            j+=1
        if _min == float('inf'):
            return -1
        return _min+1