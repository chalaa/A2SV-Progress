class Solution:
    def decodeString(self, s: str) -> str:
        def decode(i,chars,nums):

            while i < len(s):
                if s[i] == '[':
                    ch = []
                    nu = []
                    strin,i = decode(i+1,ch,nu)
                    x = "".join(nums)
                    if x:
                        strin = strin*int(x)
                        nums = []
                    chars.append(strin)
                elif s[i] == ']':
                    return "".join(chars),i
                elif s[i] in '0123456789':
                    nums.append(s[i])
                else:
                    chars.append(s[i])
                i+=1
            return "".join(chars),i
        return decode(0,[],[])[0]                
            