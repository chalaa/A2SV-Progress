class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        l=0
        r=sum(nums)
        for i in range(len(nums)):
            r -= nums[i]
            ans.append((r - ((len(nums)-i-1) *nums[i])) + nums[i]*i - l)
            l+=nums[i]
        return ans