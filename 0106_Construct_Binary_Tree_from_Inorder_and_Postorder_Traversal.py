# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        inorder(root) = inorder(node.left) -> root -> inorder(right_inorder)
        postorder(root) = postorder(node.left) -> postorder(right_inorder) -> root

        We can see the root is the last element of the postorder list,
        Before this root, we can find the right subtree.
        And before the rightsubtree, we can find the left subtree.

        Time:  O(N) --> We process each node once because additional calls are cut in O(1)
        Space: O(N) --> Space of map_val_idx_inorder O(N) +
                        N recursive calls O(N) (actually there are more, but we cut in O(1))

        """
        # As the elements are unique, we can map the values to positions
        # So we can find the elements in inorder in O(1)
        # Time to construct the dict: O(N)
        # Space for the dict: O(N)
        map_val_idx_inorder = {val: idx for idx, val in enumerate(inorder)}
        idx_postorder = len(postorder) - 1

        def buildTreeRecursively(left, right):
            """
            left -> left index (minimum index) of the inorder list
            right -> right index (maximum index) of the inorder list
            """
            if left > right:
                # The node does not have child at left or right
                return None

            nonlocal idx_postorder

            # We take the value and move to the next one, in this case, the previous one (postorder)
            node_value = postorder[idx_postorder]
            idx_postorder -= 1

            # Position in the inorder list in O(1) time
            node_idx = map_val_idx_inorder[node_value]

            node = TreeNode(node_value)

            # We assign firstly the right leaf because we are traversing the postorder list
            # decreasingly. Therefore, the next element (previous in this case), is the right
            # subtree, as exposed in the header of the function: "postorder(root)"
            node.right = buildTreeRecursively(node_idx + 1, right)

            node.left = buildTreeRecursively(left, node_idx - 1)

            return node

        return buildTreeRecursively(0, len(postorder) - 1)
