# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = defaultdict(int)
        q = deque([(root, 0)])
        
        while q:
            node, level = q.pop()
            levels[level] += node.val
            if node.left:
                q.appendleft((node.left, level + 1))
            if node.right:
                q.appendleft((node.right, level + 1))
        
        q.appendleft((root, 0, root.val))
        while q:
            node, level, siblings_val = q.pop()
            my_siblings_val = (node.left and node.left.val or 0) + (node.right and node.right.val or 0)
            node.val = levels[level] - siblings_val
            if node.left:
                q.appendleft((node.left, level + 1, my_siblings_val))
            if node.right:
                q.appendleft((node.right, level + 1, my_siblings_val))

        return root
