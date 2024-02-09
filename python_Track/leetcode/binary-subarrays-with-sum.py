class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        summation_map = defaultdict(int)
        _sum = ans = 0
        summation_map[0] += 1
        for i in nums:
            _sum += i
            if _sum - goal in summation_map:
                ans += summation_map[_sum - goal]
            summation_map[_sum] += 1
        return ans
        