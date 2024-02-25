# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node,ls):
            if not node:
                return
            ls.append(node.val)
            if node.left:
                traverse(node.left,ls)
            else:
                ls.append(None)
            if node.right:
                traverse(node.right,ls)
            else:
                ls.append(None)
        ls1 = []
        ls2 = []
        traverse(p,ls1)
        traverse(q,ls2)
        return ls1 == ls2

