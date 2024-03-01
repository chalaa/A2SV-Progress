# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)
        ans = []
        def dfs(node,depth):
            if not node:
                return
            mp[depth].append(node.val)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        for i in mp:
            if i%2:
                ans.append(reversed(mp[i]))
            else:
                ans.append(mp[i])
        return ans