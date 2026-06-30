# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, r: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return 
            if root.val == p.val or root.val == q.val:
                return root
            if root.val < p.val and root.val < q.val:
                return dfs(root.right)
            if root.val > p.val and root.val > q.val:
                return dfs(root.left)
            else:
                return root
        return dfs(r)