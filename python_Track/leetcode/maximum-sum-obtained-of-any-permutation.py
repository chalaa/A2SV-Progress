class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ## doing the range prefix sum
        ls = [0]*(len(nums)+1)
        for i in requests:
            s,e = i
            ls[s] += 1
            ls[e+1] -= 1
        ls.pop()
        for i in range(1,len(ls)):
            ls[i] += ls[i-1]
        
        ## sort both the nums and range prefix sum to -
        ## align the maximum value of the nums to the maximum no of operation
        ans = 0
        ls.sort()
        nums.sort()

        for i in range(len(nums)):
            ans += (nums[i] * ls[i])
            ans %= 1000000007
        return ans