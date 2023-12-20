class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        ct=0
        for i in nums:
            if i == 1:
                ct+=1
            else:
                mx = max(ct,mx) 
                ct=0
        mx = max(ct,mx) 
        return mx
        