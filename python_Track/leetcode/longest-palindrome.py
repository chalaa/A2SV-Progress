class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        arr = [i for i in counter.values() if i%2]
        
        if arr:
            return (len(s) - len(arr))+1
        return len(s)