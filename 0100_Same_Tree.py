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

    def isSameTree_11_08_2022(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q:
            return False
        if p and not q:
            return False
        if not q and not p:
            return True
        if p.val != q.val:
            return False
        if p.left and not q.left:
            return False
        if not p.left and q.left:
            return False
        if p.right and not q.right:
            return False
        if not p.right and q.right:
            return False
        if p.left:
            if not self.isSameTree(p.left, q.left):
                return False
        if p.right:
            if not self.isSameTree(p.right, q.right):
                return False
        return True

# Runtime: 36 ms, faster than 83.33% of Python3 online submissions for Same Tree.
# Memory Usage: 13.9 MB, less than 29.67% of Python3 online submissions for Same Tree.
