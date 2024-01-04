class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a,b):
            x = a+b
            y = b+a
            if int(x) > int(y):
                return True
            return False
        ls = [(str(i)) for i in nums]
        for i in range(1,len(ls)):
            for j in range(i,0,-1):
                if compare(ls[j],ls[j-1]):
                    ls[j],ls[j-1] = ls[j-1],ls[j]
                else:
                    break
        x = int("".join(ls))
        return str(x)
