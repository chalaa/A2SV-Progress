class Solution:
    def trap(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1][0]:
                if len(stack) > 1:
                    h = min(nums[i],stack[-2][0]) - stack[-1][0]
                    w = i - stack[-2][1] - 1
                    ans += (h*w)
                stack.pop()
            stack.append([nums[i],i])
        return ans
                

       
                    
                         