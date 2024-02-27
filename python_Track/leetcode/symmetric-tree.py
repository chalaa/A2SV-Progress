# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def traverse(leftNode,rightNode):
            if not leftNode and not rightNode:
                return True
            if (leftNode and not rightNode) or (not leftNode and rightNode):
                return False
            if leftNode.val != rightNode.val:
                return False
            return traverse(leftNode.left,rightNode.right) and traverse(leftNode.right, rightNode.left)  
        return traverse(root.left,root.right)


        