# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(deque)
        ans = []
        def dfs(node,depth):
            if not node:
                return
            if depth%2:
                mp[depth].appendleft(node.val)
            else:
                mp[depth].append(node.val)

            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        for i in mp:
                ans.append(mp[i])
        return ans