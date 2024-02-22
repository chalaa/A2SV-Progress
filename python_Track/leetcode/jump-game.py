class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        curr_jmp = 0
        while i < len(nums) and i <= curr_jmp:
            curr_jmp = max(curr_jmp,i+nums[i])
            i+=1
        if curr_jmp >= len(nums) - 1:
            return True
        return False
        