class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        n = len(palindrome)//2
        for i in range(n):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        if palindrome[-1] == 'a':
            return palindrome[:-1] + 'b'
        return palindrome[:-1] + 'a'
