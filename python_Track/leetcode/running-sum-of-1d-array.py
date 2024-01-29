class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ls = [nums[0]]
        for i in range(1,len(nums)):
            ls.append(ls[i-1]+nums[i])
        return ls