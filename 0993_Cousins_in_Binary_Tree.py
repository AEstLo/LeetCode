# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_level = None
        x_parent_val = None
        y_level = None
        y_parent_val = None

        q = deque([(root, 0, -1)])
        while q and not (x_level and y_level):
            node, level, parent_val = q.pop()
            if node.val == x:
                x_level = level
                x_parent_val = parent_val
            if node.val == y:
                y_level = level
                y_parent_val = parent_val
            if node.left:
                q.appendleft((node.left, level + 1, node.val))
            if node.right:
                q.appendleft((node.right, level + 1, node.val))
        return x_parent_val != y_parent_val and x_level == y_level
