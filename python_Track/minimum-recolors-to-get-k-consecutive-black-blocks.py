class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if k == len(blocks) :
            return blocks.count("W")
        ct = 0
        for i in range(k):
            if blocks[i] =="W":
                ct+=1
        i = 0
        j = k
        _min = ct
        while j < len(blocks):
            if blocks[j] == "W":
                ct += 1
            if blocks[i] == "W":
                ct -= 1
            i+=1
            j+=1
            _min = min(_min,ct)
        return _min     