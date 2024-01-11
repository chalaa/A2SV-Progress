class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        _min = float("inf")
        ans = 0
        for i in range(len(nums)):
            k = len(nums)-1
            j = i+1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if abs(_sum - target) < _min:
                   _min = abs(_sum - target)
                   ans = _sum
                if _min == 0:
                    return ans
                if _sum < target:
                    j+=1
                else:
                    k -=1
        return ans