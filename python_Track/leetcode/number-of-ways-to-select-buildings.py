class Solution:
    def numberOfWays(self, s: str) -> int:
        ones = zeros = 0
        one_zeros = zero_ones = ans = 0
        for i in s:
            if i == '0':
                zeros += 1
                zero_ones += ones
                ans+=one_zeros
            else:
                ones += 1
                one_zeros += zeros
                ans += zero_ones
        return ans

        