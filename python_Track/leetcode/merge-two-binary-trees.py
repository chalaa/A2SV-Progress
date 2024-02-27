# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        ## merge on the new node and return new Node
        def merge(node1,node2):
            if not node1 :
                return node2
            elif not node2:
                return node1
            newNode = TreeNode(node1.val+node2.val)
            newNode.left = merge(node1.left,node2.left)
            newNode.right = merge(node1.right,node2.right)
            return newNode
        return merge(root1,root2)

        ## merge on the root2 and return root2
        # if not root1 :
        #     return root2
        # elif not root2:
        #     return root1
        # root2.val += root1.val
        # if not root2.left:
        #     root2.left = root1.left
        #     root1.left = None
        # if not root2.right:
        #     root2.right = root1.right
        #     root1.right = None
        # self.mergeTrees(root1.left,root2.left)
        # self.mergeTrees(root1.right,root2.right)
        # return root2
        
