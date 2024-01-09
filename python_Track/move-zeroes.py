class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i=0
        # j=len(nums)-1
        # while(i<j):
        #     if nums[i]==0:
        #         nums.pop(i)
        #         nums.append(0)
        #         j-=1
        #     else:
        #         i+=1
    
        seek = 0
        found = 0
        while found < len(nums):
            if nums[found] != 0 and nums[seek] == 0:
                nums[found],nums[seek] = nums[seek],nums[found]
            if nums[seek] != 0:
                seek += 1
            found +=1
    