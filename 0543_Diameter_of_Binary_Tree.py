# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def getDiameter(node):
            nonlocal result

            if not node:
                return -1

            left = getDiameter(node.left) + 1
            right = getDiameter(node.right) + 1

            result = max(result, left + right)
            return max(left, right)

        getDiameter(root)
        return result

# Runtime: 54 ms, faster than 82.15% of Python3 online submissions for Diameter of Binary Tree.
# Memory Usage: 16.3 MB, less than 42.44% of Python3 online submissions for Diameter of Binary Tree.
