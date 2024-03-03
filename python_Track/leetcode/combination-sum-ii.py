class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = set()
        arr = []
        def findCombinationSum(ind,_sum):
            if _sum == target:
                ans.add(tuple(sorted(arr[:])))
                return
            if ind == len(candidates) or _sum > target:
                return
            for i in range(ind,len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                
                arr.append(candidates[i])
                _sum += candidates[i]
                findCombinationSum(i+1,_sum)
                _sum -= candidates[i]
                arr.pop()
        findCombinationSum(0,0)
        return ans