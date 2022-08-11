# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Time: O(N)
        # Space: O(N)
        if not root:
            return 0
        return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))

# Runtime: 76 ms, faster than 28.49% of Python3 online submissions for Maximum Depth of Binary Tree.
# Memory Usage: 16.3 MB, less than 23.50% of Python3 online submissions for Maximum Depth of Binary Tree.
