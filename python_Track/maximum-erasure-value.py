class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        _max = 0
        _set = set()
        i = 0
        j = 0
        _sum = 0
        while j < len(nums):
            while nums[j] in _set:
                _set.remove(nums[i])
                _sum -= nums[i]
                i+= 1
            _sum += nums[j]
            _set.add(nums[j])
            j+=1
            _max = max(_max,_sum)
        return _max


        