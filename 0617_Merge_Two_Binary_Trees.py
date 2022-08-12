# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root1:
            node = TreeNode(root2.val)
        elif not root2:
            node = TreeNode(root1.val)
        else:
            node = TreeNode(root1.val + root2.val)

        node.left = self.mergeTrees(
            root1.left if root1 else None, root2.left if root2 else None)
        node.right = self.mergeTrees(
            root1.right if root1 else None, root2.right if root2 else None)
        return node

# Runtime: 149 ms, faster than 39.21% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 15.5 MB, less than 46.70% of Python3 online submissions for Merge Two Binary Trees.
