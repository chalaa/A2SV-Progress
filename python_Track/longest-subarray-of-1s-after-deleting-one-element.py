class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        max_val = 0
        zero = -1
        counter = 0
        while j < len(nums):
            if nums[j] == 0:
                if counter == 0:
                    counter += 1
                    zero = j
                else:
                    i = zero + 1
                    zero = j
            j += 1
            max_val = max(max_val, j - i - 1)

        return max_val