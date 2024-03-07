# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)
        def dfs(node,col,row):
            if not node:
                return
            mp[col].append((row,node.val))

            dfs(node.left,col-1,row+1)
            dfs(node.right,col+1,row+1)
        dfs(root,0,0)

        sorted_key = sorted(mp.keys())
        ans = []
        for i in sorted_key:
            mp[i].sort()
            temp = []
            for j in mp[i]:
                temp.append(j[1])
            ans.append(temp)
        return ans
