# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ct = 0
        _min = -1
        def inorder(node,k):
            nonlocal ct
            nonlocal _min
            if not node:
                return 
            inorder(node.left,k)
            ct+=1
            if ct == k:
                _min = node.val
            inorder(node.right,k)
        inorder(root,k)
        return _min