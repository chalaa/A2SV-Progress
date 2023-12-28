class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        st = sorted(nums)
        dic = {}
        ans = []
        j=len(nums)-1
        while j > -1:
            i = j
            while i > -1 and st[i] == st[j]:
                i-=1
            dic[st[j]] = i+1
            j = i
        for i in nums:
            ans.append(dic[i])
        return ans
                