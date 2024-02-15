class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        i = len(nums)-2
        while i > -1:
            if nums[i]>nums[i+1]:
                ## get the total number of elements that we can devide it in to
                total_element = ceil(nums[i]/nums[i+1])
                ## add total operation needed to break down
                ans += total_element - 1
                ## get the updated last element after breakdown
                nums[i] //= ceil(nums[i]/nums[i+1])
            i-=1
        return ans

