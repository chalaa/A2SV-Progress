class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ans = "".join(i for i in s if i.isalnum())
        print(ans)
        i=0
        j=len(ans)-1
        while i<j:
            if ans[i] != ans[j]:
                return False
            i += 1 
            j -= 1
        return True