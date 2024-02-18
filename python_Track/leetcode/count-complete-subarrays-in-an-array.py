class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        st = set(nums)
        ans = 0
        mp = defaultdict(int)
        l = 0
        n = len(nums)
        for i in range(n):
            mp[nums[i]] += 1
            while len(st) == len(mp.keys()):
                ans += n - i
                mp[nums[l]] -= 1
                if mp[nums[l]] == 0:
                    del(mp[nums[l]])
                l+=1
        return ans
