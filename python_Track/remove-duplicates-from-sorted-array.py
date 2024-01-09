class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # st = sorted(set(nums))
        # for i in range(len(st)):
        #     nums[i] = st[i]
        # for j in range(i+1,len(nums)):
        #     nums[j] = "_"
        # return len(st)
        i = 1
        j = 1
        while j < len(nums):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
            j+=1
        return i