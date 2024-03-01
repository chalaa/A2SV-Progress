class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        ans.add(())
        arr = []
        def find(ind):
            if ind == len(nums):
                return
            for i in range(ind,len(nums)):
                arr.append(nums[i])
                ans.add(tuple(sorted(arr[:])))
                find(i+1)
                arr.pop()
        find(0)
        return ans

        