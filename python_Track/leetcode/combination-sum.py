class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        arr = []
        def find(ind,_sum):
            if _sum == target:
                ans.add(tuple(sorted(arr[:])))
                return
            if ind == len(candidates) or _sum > target:
                return
            for i in range(ind,len(candidates)):
                arr.append(candidates[i])
                _sum += candidates[i]
                find(i,_sum)
                _sum -= candidates[i]
                arr.pop()
        find(0,0)
        return ans
