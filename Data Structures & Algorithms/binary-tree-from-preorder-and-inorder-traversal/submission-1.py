class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hash = {}
        for i, ele in enumerate(inorder):
            inorder_hash[ele] = i

        self.pre_idx = 0  # pointer into preorder, always points to the "next root"

        def create_tree(left, right):
            # left, right are index bounds into the ORIGINAL inorder array (inclusive)
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            mid = inorder_hash[root_val]  # position of root in inorder — a real global index now

            root.left = create_tree(left, mid - 1)
            root.right = create_tree(mid + 1, right)
            return root

        return create_tree(0, len(inorder) - 1)