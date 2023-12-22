class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        sm = defaultdict(list)
        dp = defaultdict(int)
        ans = []
        for i in range(len(list1)):
            sm[list1[i]].append(i)
        for i in range(len(list2)):
            sm[list2[i]].append(i)
        for k in sm:
            if len(sm[k]) == 2:
                dp[k] = sum(sm[k])
        mn = min(dp.values())
        for k,v in dp.items():
            if v==mn:
                ans.append(k)
        return ans

        