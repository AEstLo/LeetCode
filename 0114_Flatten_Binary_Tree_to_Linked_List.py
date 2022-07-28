# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Time: O(N)
        # Space: O(N) -> recursion calls

        def rightMost(root):
            node = root
            while node.right:
                node = node.right
            return node

        def reAssignLeftChild(node, parent):
            if node:
                reAssignLeftChild(node.left, node)
                if parent and parent.left == node:
                    right_most_node = rightMost(node)
                    right_most_node.right = parent.right
                    parent.right = node
                    parent.left = None
                reAssignLeftChild(node.right, node)

        reAssignLeftChild(root, None)

    def preorder(self, root):
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

# Runtime: 48 ms, faster than 73.04% of Python3 online submissions for Flatten Binary Tree to Linked List.
# Memory Usage: 15.4 MB, less than 10.29% of Python3 online submissions for Flatten Binary Tree to Linked List.
