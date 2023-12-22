class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        ct = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                ct += 1
                if ct > 1:
                    return False
                if i >= 2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
        return True
        