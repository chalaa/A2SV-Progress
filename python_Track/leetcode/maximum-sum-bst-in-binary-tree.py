# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxSumBST(self, root: Optional[TreeNode]) -> int:
#         _sum = 0
#         def dfs(node):
#             nonlocal _sum 
#             if not node:
#                 return (float('-inf'), float('inf'), 0)
#             l = dfs(node.left)
#             r = dfs(node.right)
#             print(node.val,l,r)
#             if l[0] < node.val and node.val <r[1]:
#                 ans = l[-1] + r[-1] + node.val
#                 _sum = max(_sum,ans)
#                 return ( min( node.val ,l[1] ), max( node.val ,r[0] ),ans)
#             return (float('-inf'),float('inf'),max(l[-1],r[-1]))
#         dfs(root)
#         return _sum


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.ans = 0
        
        def maxSum(root):
            if not root:
                return True, [float('inf'), float('-inf')], 0
            
            l, l_range, l_sum = maxSum(root.left)
            r, r_range, r_sum = maxSum(root.right)
            
            if l and r and l_range[1] < root.val < r_range[0]:
                total = l_sum + r_sum + root.val
                self.ans = max(self.ans, total)
                return True, [min(l_range[0], root.val), max(r_range[1], root.val)], total
            
            return False, [float('inf'), float('-inf')], None
        
        _, __, ___ = maxSum(root)
        return self.ans