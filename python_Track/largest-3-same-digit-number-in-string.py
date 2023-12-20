class Solution:
    def largestGoodInteger(self, num: str) -> str:
        mx = -1
        for i in range(len(num)-2):
            if len(set(num[i:i+3])) == 1:
                mx = max(int(num[i]),mx)
        if mx == -1:
            return ""
        return str(mx)*3
