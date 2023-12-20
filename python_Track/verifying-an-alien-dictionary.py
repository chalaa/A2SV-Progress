class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        j=0
        mp = {}
        for i in order:
            mp[i] = j
            j+=1
        for j in range(len(words)-1):
            mn = min(len(words[j+1]),len(words[j]))
            ct = 0
            for i in range(mn):
                if mp[words[j][i]] == mp[words[j+1][i]]:
                    ct+=1
                    continue
                elif mp[words[j][i]] < mp[words[j+1][i]]:
                    break
                else:
                    return False
            if ct == mn and len(words[j+1]) < len(words[j]):
                return False
        return True



