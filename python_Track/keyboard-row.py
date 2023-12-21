class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        key = [set("eiopqrtuwy"),set("adfghjkls"),set("bcmnvxz")]
        ans = []
        for i in words:
            for j in key:
                for k in set(i):
                    if k.lower() not in j:
                        break
                else:
                    ans.append(i)
                    break
        return ans