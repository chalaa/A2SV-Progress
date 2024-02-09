class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        mp = defaultdict(int)
        mp[0] += 1
        _sum = 0
        for i in nums:
            _sum += i
            if _sum%k in mp:
                ans += mp[_sum%k]
            mp[_sum%k] += 1
        return ans