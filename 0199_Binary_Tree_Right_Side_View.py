# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Being N the number of nodes of the tree
        # Time: O(N)
        # Space: O(log(N))
        if not root:
            return []
        q = collections.deque()
        q.append((root, 0))
        rightmost_node = [-1] * 101  # There are at most 100 nodes
        while q:
            node, level = q.pop()
            rightmost_node[level] = node.val
            if node.left:
                q.appendleft((node.left, level + 1))
            if node.right:
                q.appendleft((node.right, level + 1))
        i = 0
        result = []
        while i < 101 and rightmost_node[i] != -1:
            result.append(rightmost_node[i])
            i += 1

        return result
