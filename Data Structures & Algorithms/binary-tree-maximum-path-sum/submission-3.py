# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left) 
            right = dfs(node.right)
            path_sum = node.val + left + right
            res = max(res , path_sum , node.val , node.val + left , node.val + right)
            return max(node.val , node.val + max(left , right))
        dfs(root)
        return res
