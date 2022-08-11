# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Time: O(N)
        # Space: O(N)
        def recursion(node, min_val=None, max_val=None):

            if not node:
                return True
            if node.left and node.val <= node.left.val or (min_val and min_val >= node.val) or not recursion(node.left, min_val=min_val, max_val=node.val):
                return False
            if node.right and node.val >= node.right.val or (max_val and max_val <= node.val) or not recursion(node.right, min_val=node.val, max_val=max_val):
                return False
            return True

        return recursion(root)

# Runtime: 56 ms, faster than 76.91% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.6 MB, less than 46.02% of Python3 online submissions for Validate Binary Search Tree.
