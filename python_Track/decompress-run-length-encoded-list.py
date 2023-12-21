class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)//2):
            ans += [nums[2*i+1]] * nums[2*i]
        return ans