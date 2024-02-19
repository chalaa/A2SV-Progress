class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ls=[]
        op = ["*","/","-","+"]
        for i in tokens:
            if(i not in op):
                ls.append(int(i))
            else:
                a = ls.pop()
                b = ls.pop()
                if(i=="*"):
                    ls.append(a*b)
                elif(i=="+"):
                    ls.append(a+b)
                elif(i=="/"):
                    ls.append(int(b/a))
                elif(i=="-"):
                    ls.append(b-a)
        return ls[0]