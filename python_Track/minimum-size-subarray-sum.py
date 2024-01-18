class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        _min = float("inf")
        sum=nums[0]
        i=0
        j=1
        while i<j:
            if sum>=target:
                _min = min(_min,(j-i))
                sum-=nums[i]
                i+=1
            else:
                if j<len(nums):
                    sum+=nums[j]
                    j+=1
                if j==len(nums) and sum<target:
                    break
        if _min != float("inf"):
            return _min
        return 0