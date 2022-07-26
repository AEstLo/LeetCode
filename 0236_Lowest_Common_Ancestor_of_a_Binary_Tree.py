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
        # Runtime: 130 ms, faster than 29.17% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
        # Memory Usage: 26.3 MB, less than 30.85% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
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

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time: O(N)
        # Space: O(N)
        # Runtime: 153 ms, faster than 13.99% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
        # Memory Usage: 26.4 MB, less than 30.85% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
        def dfs(node, val, path):
            if not node:
                return False
            if node.val == val:
                path.append(node)
                return True
            left = dfs(node.left, val, path)
            if left:
                path.append(node)
                return True
            right = dfs(node.right, val, path)
            if right:
                path.append(node)
                return True
            return False

        path_p = []
        dfs(root, p.val, path_p)
        path_q = []
        dfs(root, q.val, path_q)

        idx_p = len(path_p) - 1
        idx_q = len(path_q) - 1
        while idx_p >= 0 and idx_q >= 0 and path_p[idx_p].val == path_q[idx_q].val:
            idx_p -= 1
            idx_q -= 1
        return path_p[idx_p + 1]
