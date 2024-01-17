class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ct = nums.count(val)
        i = 0
        j = len(nums) - 1
        while i < len(nums)-ct:
            if nums[i] == val:
                while j > i and nums[j] == val:
                    j-=1
                nums[i],nums[j] = nums[j],nums[i]
            i+=1
        return len(nums) - ct



        