# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Time: O(N)
        # Space: O(N)
        queue = collections.deque([(root, 0)])
        levels = collections.defaultdict(list)

        while queue:
            node, level = queue.pop()
            levels[level].append(node.val)

            if node.left:
                queue.appendleft((node.left, level + 1))
            if node.right:
                queue.appendleft((node.right, level + 1))

        result = [0] * len(levels)
        for level in levels:
            result[level] = sum(levels[level])/len(levels[level])
        return result

# Runtime: 53 ms, faster than 92.62% of Python3 online submissions for Average of Levels in Binary Tree.
# Memory Usage: 16.5 MB, less than 47.59% of Python3 online submissions for Average of Levels in Binary Tree.
