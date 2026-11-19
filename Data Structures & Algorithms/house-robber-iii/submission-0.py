# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def function(node):
            if not node:
                return [0 , 0]
            [left_with_root , left_without_root] = function(node.left)
            [right_with_root , right_without_root] = function(node.right)
            # With the node Included 
            node_included = node.val + left_without_root + right_without_root
            # Without the node Included
            node_excluded = max(left_with_root , left_without_root) + max(right_with_root , right_without_root)
            return [node_included , node_excluded]
        return max(function(root))