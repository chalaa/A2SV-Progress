class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        best = right
        while left<= right:
            mid = left + (right-left)//2
            count = 1
            _sum = 0
            for i in nums:
                if _sum + i > mid: 
                    _sum = 0
                    count += 1
                _sum += i
            if count > k:
                left = mid +1
            else:
                right = mid -1 

        return left