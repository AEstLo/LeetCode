# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if root.val < 2:  # leaf node
            return 1 == root.val
        if not root.left or not root.right:
            return False
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 2:  # or
            return left or right
        if root.val == 3:  # and
            return left and right
        return False
