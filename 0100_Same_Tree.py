# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Being P the number of nodes of p and Q the number of nodes of q
        # Time: O(min(P, Q))
        # Space: O(min(P, Q))
        def dfsDouble(root1, root2):
            if not root1 and not root2:
                return True
            if (root1 and not root2) or (not root1 and root2):
                return False
            if root1.val != root2.val:
                return False
            return dfsDouble(root1.left, root2.left) and dfsDouble(root1.right, root2.right)

        return dfsDouble(p, q)

# Runtime: 44 ms, faster than 59.23% of Python3 online submissions for Same Tree.
# Memory Usage: 14 MB, less than 29.45% of Python3 online submissions for Same Tree.
