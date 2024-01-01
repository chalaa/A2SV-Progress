class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num > 0:
            ls = list(str(num))
            ls.sort()
            i =0
            ans = ""
            while i < len(ls) and ls[i] == '0':
                i+=1
            ans += ls[i]
            for j in range(i):
                ans+=ls[j]
            i+=1
            while i < len(ls):
                ans += ls[i]
                i+=1
            return int(ans)
        else:
            ls = sorted(list(str(num))[1:], reverse=True)
            ans = "".join(ls)
            return -int(ans)
        