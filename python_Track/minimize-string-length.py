class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len({i for i in s})