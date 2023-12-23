class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mx = 0
        nums.sort()
        j=1
        ct = 1
        if len(nums) == 0:
            return 0
        while j<len(nums):
            if nums[j] - nums[j-1] == 1:
                j += 1
                ct += 1
            elif nums[j] == nums[j-1]:
                j += 1
                continue
            else:
                mx = max(mx,ct)
                ct=1
                j+=1
        mx = max(mx,ct)
        return mx
