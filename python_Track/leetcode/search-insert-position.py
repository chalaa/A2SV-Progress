class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while j>=i:
            md=i + (j-i)//2
            if nums[md]<target:
                i = md+1
            elif nums[md]>target:
                j=md-1
            else:
                return md
        return i