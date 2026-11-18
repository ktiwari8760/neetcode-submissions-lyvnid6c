# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def function(node):
            if not node:
                return 0
            left = function(node.left)
            right = function(node.right)

            if left == -1:
                return -1
            if right == -1:
                return -1
            if abs(right - left) > 1:
                return -1
            
            return 1 + max(right , left)
        
        return function(root) != -1