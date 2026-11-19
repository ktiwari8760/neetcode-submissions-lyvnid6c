# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        heap = []
        heapq.heapify(heap)

        def dfs(node):
            nonlocal heap
            if not node:
                return 
            heapq.heappush(heap , node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        ans = -1
        while k > 0:
            ans = heapq.heappop(heap)
            k -= 1
        return ans
    