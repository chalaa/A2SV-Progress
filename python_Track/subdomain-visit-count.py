class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = defaultdict(int)
        ans = []
        for i in cpdomains:
            s = i.split()
            mp[s[1]] += int(s[0])
            x = s[1]
            ct = x.find('.')
            while ct != -1:
                x = x[ct+1:]
                mp[x] += int(s[0])
                ct = x.find('.')
        for k,v in mp.items():
            ans.append(f"{v} {k}")
        return ans
                