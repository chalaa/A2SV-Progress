class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        for i in houses:
            left = bisect_left(heaters,i)
            temp = float("inf")

            if left > 0:
                temp =i - heaters[left-1]
            if left < len(heaters):
                temp = min(heaters[left]-i,temp)
            print(temp,left,i,ans)
            ans = max(ans,temp)
        return ans