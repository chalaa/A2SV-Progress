class Solution:
    def largestOddNumber(self, num: str) -> str:
        j=len(num)-1
        while j>=0:
            if int(num[j])%2:
                return num[0:j+1]
            j-=1
        return ""