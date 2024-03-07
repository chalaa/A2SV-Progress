class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0

        for i in range(len(nums)):
            left = i
            right = len(nums)-1
            while left <= right:
                mid = left + (right-left)//2

                if nums[i] + nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid-1
            if left > i:
                n = left - i - 1
                ans += pow(2,n,1000000007)
                ans %= 1000000007
                   
        return ans