class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = [i for i in nums if i < pivot]
        p = [i for i in nums if i == pivot]
        r = [i for i in nums if i > pivot]
        return l+p+r
        