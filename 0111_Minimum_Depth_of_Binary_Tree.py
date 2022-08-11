# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Time: O(N)
        # Space: O(N)
        if not root:
            return 0
        queue = collections.deque([(root, 1)])

        while queue:
            node, level = queue.pop()

            if not node.left and not node.right:
                return level

            if node.left:
                queue.appendleft((node.left, level + 1))
            if node.right:
                queue.appendleft((node.right, level + 1))
        # This code should never be reached
        return -1

# Runtime: 862 ms, faster than 46.85% of Python3 online submissions for Minimum Depth of Binary Tree.
# Memory Usage: 49.3 MB, less than 79.48% of Python3 online submissions for Minimum Depth of Binary Tree.
