class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mp = {}
        #add prefix sum for each value in the list
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]].append(mp[nums[i]][-1] + i)
            else:
                mp[nums[i]] = [0,i]
        
        # initialize the dictionary to count the frequency of each elemnt in the list
        mp_ct = defaultdict(int)
        ans = []
        #iterate over the list
        for i in nums:
            #increment the list frequency
            mp_ct[i] += 1
            pt = mp_ct[i]

            #get the prefixsum for the specific value in the list
            prefix = mp[i]
            #calculate the sum distance from the prefixsum array
            val = prefix[pt]-prefix[pt-1]
            left = (pt-1)*(val) - prefix[pt-1]
            right = (prefix[-1] - prefix[pt]) - val*(len(prefix)-pt-1)
            ans.append(left+right)
        return ans
