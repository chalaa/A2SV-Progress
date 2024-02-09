class Solution:
    def maxScore(self, s: str) -> int:
        # ct_0 = [0]
        # ct_1 = [0]
        # ans = 0
        # for i in s:
        #     if i == "0":
        #         ct_0.append(ct_0[-1]+1)
        #         ct_1.append(ct_1[-1])
        #     else:
        #         ct_1.append(ct_1[-1]+1)
        #         ct_0.append(ct_0[-1])
        # n = len(s)
        # for i in range(1,n):
        #      ans = max((ct_1[n] - ct_1[i] + ct_0[i]), ans)
        # return ans
        
        left = 0
        right = s.count("1")
        _max = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                left+=1
            else:
                right-=1
            _max = max(_max,(left+right))
        return _max