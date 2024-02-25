# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mp = defaultdict(int)
        res = []
        def dfs(node):
            if not node: 
                return
            nonlocal mp
            dfs(node.left)
            mp[node.val] += 1
            dfs(node.right)
        dfs(root)
        _max = max(mp.values())
        for i in mp:
            if mp[i] == _max:
                res.append(i)
        return res