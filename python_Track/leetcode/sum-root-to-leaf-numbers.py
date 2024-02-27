# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node,s):
            if not node.left and not node.right:
                s += str(node.val)
                self.ans += int(s)
                return
            if node.left:
                dfs(node.left,s+str(node.val))
            if node.right:
                dfs(node.right,s+str(node.val))
        dfs(root,"")
        return self.ans
        