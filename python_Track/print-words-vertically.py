class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        mx= [0,0]
        ls = []
        for i in range(len(s)):
            if len(s[i]) >= mx[0]:
                mx[0]=len(s[i])
                mx[1] = i
        for i in range(mx[0]):
            st =""
            for j in range(len(s)):
                if len(s[j]) > i:
                    st+=s[j][i]
                else:
                    st+=" "
            st = st.rstrip()
            ls.append(st)
        return ls

        