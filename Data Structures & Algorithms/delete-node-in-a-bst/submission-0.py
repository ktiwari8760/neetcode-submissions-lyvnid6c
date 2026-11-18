# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(node , key):
            if not node:
                return None
            if node.val == key:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                else:
                    temp = node.right
                    while temp.left:
                        temp = temp.left
                    node.val= temp.val
                    node.right = dfs(node.right , temp.val)
            if node.val < key:
                node.right = dfs(node.right , key)
            else:
                node.left = dfs(node.left , key)
            return node
        return dfs(root , key)