class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left=1
        right = k
        sm = sum(nums[0:k])
        mx=sm
        while right<len(nums):
            sm = sm-nums[left-1]+nums[right]
            mx = max(mx,sm)
            left+=1
            right+=1
        return mx/k
