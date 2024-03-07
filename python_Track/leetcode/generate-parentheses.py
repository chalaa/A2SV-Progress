class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res=[]
        st=[]
        def eachParentesis(op,cl):
            if op==cl==n:
                res.append("".join(st))
                return
            if op<n:
                st.append("(")
                eachParentesis(op+1,cl)
                st.pop()
            if cl< op:
                st.append(")")
                eachParentesis(op,cl+1)
                st.pop()
        eachParentesis(0,0)
        return res
            