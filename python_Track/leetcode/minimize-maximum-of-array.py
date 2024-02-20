class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        _sum = _max = nums[0]
        for i in range(1,len(nums)):
            if _max < nums[i]:
                x = (((nums[i]*i)-_sum))//(i+1)
                _max = max(_max,nums[i]-x)
            _sum += nums[i]
        return _max