class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        ans = 0
        while i < j:
            if nums[i] + nums[j] >= target:
                j -= 1
            else:
                ans += (j-i)
                i += 1
        return ans

        