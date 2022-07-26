# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time: O(N)
        # Space: O(N)
        if root == p or root == q:
            return root
        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right

# Runtime: 130 ms, faster than 29.17% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
# Memory Usage: 26.3 MB, less than 30.85% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
