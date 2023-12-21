class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i=0
        while i < len(command):
            if command[i] != '(':
                ans+=command[i]
            else:
                j=i
                while command[j] != ')':
                    j+=1
                if j-i == 1:
                    ans+='o'
                else:
                    ans+=command[i+1:j]
                i=j
            i+=1
        return ans

        
        