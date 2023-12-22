class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        mx = len(nums)//3
        ans = []
        for k,v in counter.items():
            if v > mx:
                ans.append(k)
        return ans