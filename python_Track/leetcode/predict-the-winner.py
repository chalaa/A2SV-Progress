class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def perm(left,right):
            if left == right:
                return nums[left]
            left_rec = nums[left] - perm(left+1,right)
            right_rec = nums[right] - perm(left,right-1)
            return max(left_rec,right_rec)
            
        return perm(0,len(nums)-1) >= 0
