# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(node1,node2):
            if not node1 and not node2:
                return None
            elif not node1 and node2:
                return node2
            elif node1 and not node2:
                return node1
            node2.val += node1.val
            if not node2.left:
                node2.left = node1.left
                node1.left = None
            if not node2.right:
                node2.right = node1.right
                node1.right = None
            merge(node1.left,node2.left)
            merge(node1.right,node2.right)
            return node2
        return merge(root1,root2)
