class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        _sum,count = 0,0
        i = 0
        while _sum < n:
            if i < len(nums) and _sum+1 >= nums[i]:
                _sum += nums[i]
                i+=1
            else:
                count += 1
                _sum += (_sum+1)
        return count