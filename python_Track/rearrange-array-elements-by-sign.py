class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pt = [i for i in nums if i>0]
        ng = [i for i in nums if i<0]
        ans = []
        for i in range(len(pt)):
            ans.append(pt[i])
            ans.append(ng[i])
        return ans