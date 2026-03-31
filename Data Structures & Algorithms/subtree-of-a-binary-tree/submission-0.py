# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def function1(node1 , node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            return function1(node1.left , node2.left) and function1(node1.right , node2.right)
        
        def function2(root ,subRoot ):
            if root is None :
                return False
            if function1(root , subRoot):
                return True
            return function2(root.left , subRoot) or function2(root.right , subRoot)
        return function2(root,subRoot)
            

            