# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        queue = deque([root])
        answer = []
        while queue:
            level = []
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.popleft()
                level.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            answer.append(level[0])
        return answer