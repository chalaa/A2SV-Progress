class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        _max=0
        ct = 0
        pt = 0
        ind = []
        while j  < len(nums):
            if nums[j] == 0:
                ind.append(j+1)
                ct+=1
                if ct > k:
                    i = ind[pt]
                    pt += 1
                    ct -= 1
            _max = max(_max,(j-i+1))
            j+=1
        return _max


