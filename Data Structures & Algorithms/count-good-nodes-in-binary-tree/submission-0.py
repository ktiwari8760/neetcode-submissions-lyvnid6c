# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        def helper(node , path_max):
            nonlocal counter
            if not node:
                return
            if node.val >= path_max:
                path_max = node.val
                counter += 1
            helper(node.left , path_max)
            helper(node.right , path_max)
        helper(root , float('-inf'))
        return counter