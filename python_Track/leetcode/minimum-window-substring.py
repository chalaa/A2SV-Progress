class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if len(t) == 1 and t[0] in s:
            return t
        t_counter = Counter(t)
        s_counter = defaultdict(int)
        for i in range(len(t)-1):
            s_counter[s[i]] += 1
        i = 0
        j = len(t)-1
        ls = []
        while j < len(s):
            flag = True
            for k in t_counter:
                if t_counter[k] > s_counter[k]:
                    flag = False
                    break
            if flag:
                ls.append((j-i, i , j))
                s_counter[s[i]] -= 1
                i += 1
            else:
                s_counter[s[j]] += 1
                j += 1
        while i < len(s):
            flag = True
            for k in t_counter:
                if t_counter[k] > s_counter[k]:
                    flag = False
                    break
            if flag:
                ls.append((j-i, i , j))
                s_counter[s[i]] -= 1
                i += 1
            else:
                break
        ls.sort()
        print(ls)
        if ls:
            a,b,c = ls[0]
            ans = ""
            for i in range(b,c):
                ans+=s[i]
            return ans
        return ""
        