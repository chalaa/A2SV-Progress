class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sm = 0
        ans = []
        for i in nums:
            if i%2==0:
                sm+=i
        for i in queries:
            x = nums[i[1]]
            nums[i[1]] += i[0]
            if x % 2 == 0:
                sm -= x
            if nums[i[1]] % 2 == 0:
                sm += nums[i[1]]
            ans.append(sm)
        return ans

        