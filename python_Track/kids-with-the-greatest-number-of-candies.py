class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        ls=[]
        for i in candies:
            if i + extraCandies >= mx:
                ls.append(True)
            else:
                ls.append(False)
        return ls
        