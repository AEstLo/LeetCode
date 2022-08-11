# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if targetSum == root.val and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

# Runtime: 51 ms, faster than 81.89% of Python3 online submissions for Path Sum.
# Memory Usage: 15 MB, less than 57.88% of Python3 online submissions for Path Sum.
