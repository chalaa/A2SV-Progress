# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def makeTree(start,end):
            if start>end:
                return
            mid = (start+end)//2
            return TreeNode(nums[mid],makeTree(start,mid-1),makeTree(mid+1,end))
            
        return makeTree(0,len(nums)-1)
        