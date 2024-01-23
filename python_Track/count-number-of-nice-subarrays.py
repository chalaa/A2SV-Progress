class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        odds = []
        for i in range(len(nums)):
            if nums[i]%2:
                odds.append(i)
        
        left = 0
        right = k-1

        while right < len(odds):
            left_count = 0
            if left > 0:
                left_count = odds[left] - odds[left-1] - 1
            else:
                left_count = odds[left]
            right_count = 0
            if right < len(odds)-1:
                right_count = odds[right+1] - odds[right] - 1
            else:
                right_count = len(nums) - (odds[right] + 1)

            ans += (left_count+1) * (right_count+1)
            left += 1
            right += 1
        return ans

