class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_sum = [0]
        for i in nums:
            prefix_sum.append(prefix_sum[-1] + i)
        if prefix_sum[-1]%p == 0:
            return 0
        else:
            t = prefix_sum[-1]%p
            _min = float('inf')
            dic = {0:-1}
            for i in range(len(prefix_sum)):
                dic[prefix_sum[i]%p] = i
                if (prefix_sum[i] - t) % p in dic:
                    _min = min(_min,i-dic[(prefix_sum[i] - t) % p])

            if _min >= len(nums):
                return -1
            return _min