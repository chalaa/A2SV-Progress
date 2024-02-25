# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        def rec(node):
            if not node:
                return 
            if low <= node.val <= high:
                self.total += node.val
                rec(node.left)
                rec(node.right)
            elif node.val < low:
                rec(node.right)
            else:
                rec(node.left)
        rec(root)
        return self.total