class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        st = defaultdict(list)
        ans = []
        for i in paths:
            x = i.split()
            for i in range(1, len(x)):
                ind = x[i].find('(')
                fi = x[i][ind:-1]
                name = x[i][:ind]
                path = x[0]+"/"+name
                st[fi].append(x[0]+"/"+name)
        for v in st.values():
            if len(v) > 1:
                ans.append(v)
        return sorted(ans,key=lambda x: len(x))
        