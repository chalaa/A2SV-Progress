class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # ct=0
        # i=0
        # j=len(piles)-2
        # piles.sort()
        # while j>i:
        #     ct+=piles[j]
        #     j-=2
        #     i+=1
        # return ct

        piles.sort()
        ans = 0
        i = len(piles) // 3
        for j in range(i,len(piles),2):
            ans+=piles[j]
        return ans
