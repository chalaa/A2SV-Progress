class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        ps = defaultdict(int)
        for i in p:
            ps[i]+=1
        sp =defaultdict(int)
        for i in range(len(p)):
            sp[s[i]]+=1
        i=0
        j=len(p)
        res = []
        if sp==ps:
            res.append(i)
        while j<len(s):
            sp[s[i]]-=1
            sp[s[j]]+=1
            if sp[s[i]] == 0:
                del(sp[s[i]])
            i+=1
            j+=1
            if sp==ps:
                res.append(i)
        return res
