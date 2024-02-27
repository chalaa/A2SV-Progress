# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            if not node.right and not node.left:
                return (0,node.val,node.val)
            ans = 0
            _min = float("inf")
            _max = -1
            if node.left:
                a = rec(node.left)
                ans = max(ans,a[0])
                _min = min(_min,a[1])
                _max = max(_max,a[2])
            if node.right:
                a = rec(node.right)
                ans = max(ans,a[0])
                _min = min(_min,a[1])
                _max = max(_max,a[2])
            return(max(ans,abs(node.val - _max),abs(node.val - _min)), min(node.val,_min), max(node.val, _max))

        return rec(root)[0]
            

        