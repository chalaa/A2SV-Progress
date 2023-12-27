class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeros = [0]
        ones = [0]
        for i in nums:
            if i == 0:
                zeros.append(zeros[-1]+1)
                ones.append(ones[-1])
            else:
                zeros.append(zeros[-1])
                ones.append(ones[-1]+1)
        
        ans = defaultdict(list)
        n = len(nums)
        
        for i in range(len(zeros)):
            ans[zeros[i] + (ones[n]-ones[i])].append(i)
        
        return ans[max(ans)]
