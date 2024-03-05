# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def inorder_traverse(node):
            if not node:
                return
            inorder_traverse(node.left)
            ans.append(node.val)
            inorder_traverse(node.right)

        inorder_traverse(root)

        def merge(left,right):
            if left > right:
                return
            mid = (left+right)//2
            return TreeNode(ans[mid],merge(left,mid-1),merge(mid+1,right))

        return merge(0,len(ans)-1)
        
        