class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]].append(mp[nums[i]][-1] + i)
            else:
                mp[nums[i]] = [0,i]
        mp_ct = defaultdict(int)
        ans = []

        for i in nums:
            mp_ct[i] += 1
            pt = mp_ct[i]
            prefix = mp[i]
            if len(prefix) > 2:
                val = prefix[pt]-prefix[pt-1]
                left = (pt-1)*(val) - prefix[pt-1]
                right = (prefix[-1] - prefix[pt]) - val*(len(prefix)-pt-1)
                ans.append(left+right)
            else:
                ans.append(0)
        return ans
