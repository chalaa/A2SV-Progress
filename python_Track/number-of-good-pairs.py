class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=0
        counter = Counter(nums)
        for v in counter.values():
            if v > 1:
                ans+=(v*(v-1))/2
        return int(ans)
        