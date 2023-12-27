class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mp = {heights[i]:names[i] for i in range(len(names))}
        ans = []
        for i in sorted(mp.keys(), reverse=True):
            ans.append(mp[i])
        return ans