class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        def eql(a:dict, b:defaultdict(int)):
            for k in a:
                if a[k] != b[k]:
                    return False
            return True
        mp_1 = Counter(s1)
        mp_2 = defaultdict(int)
        for i in range(len(s1)):
            mp_2[s2[i]] +=1
        if eql(mp_1,mp_2):
            return True
        i=0
        j=len(s1)
        while j < len(s2):
            mp_2[s2[i]] -=1
            mp_2[s2[j]] +=1
            if eql(mp_1,mp_2):
                return True
            i+=1
            j+=1
        return False