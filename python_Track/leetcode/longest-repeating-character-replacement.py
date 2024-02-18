class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        l = 0
        r = 0
        _max = 0
        while r < len(s):
            counter[s[r]] += 1
            while r - l + 1 - max(counter.values()) > k:
                counter[s[l]] -= 1
                l+=1
            _max = max(_max,r-l+1)
            r+=1
        
        return _max


           

            
