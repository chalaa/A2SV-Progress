class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = [[]]
        def backtrack(arr,ind):
            if ind == len(nums):
                return
            for i in range(ind,len(nums)):
                arr.append(nums[i])
                self.ans.append(arr[:])
                backtrack(arr,i+1)
                arr.pop()
        backtrack([],0)
        return self.ans