class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        right = float('-inf')
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] < nums[i]:
                right = max(right,stack.pop())
            if nums[i] < right:
                return True
            stack.append(nums[i])
        return False

        