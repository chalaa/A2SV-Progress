class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left <= right:
            mid = left + (right-left)//2
            
            temp_sum = 0
            for i in nums:
                temp_sum += ceil(i/mid)
            
            if temp_sum <= threshold:
                right = mid-1
            else:
                left = mid + 1
        return left