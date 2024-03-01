class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        ## backtracking without extra space
        def backtrack(ind):
            if ind == len(nums):
                self.ans.append(nums[:])
            for i in range(ind,len(nums)):
                nums[i],nums[ind] = nums[ind],nums[i]
                backtrack(ind+1)
                nums[i],nums[ind] = nums[ind],nums[i]
        backtrack(0)
        return self.ans
        