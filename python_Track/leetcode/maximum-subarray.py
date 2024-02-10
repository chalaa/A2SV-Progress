class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # mx=x=nums[0]
        # for i in range(1,len(nums)):
        #     x+=nums[i]
        #     if x<nums[i]:
        #         x=nums[i]
        #     mx=max(mx,x)
        # return mx
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + i)
        _max = max(prefix[1:])
        _min = 0
        for i in range(1,len(prefix)):
            _max = max(_max,(prefix[i]-_min))
            _min = min(_min,prefix[i])
        return _max