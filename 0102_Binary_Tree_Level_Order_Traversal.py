# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Being N the number of nodes in the tree
        # Time: O(N)
        # Space: O(N)
        if not root:
            return []
        level = 0
        queue = [(root, level)]
        list_aux = []
        result = []
        while queue:
            for node, level in queue:
                while len(result) <= level:
                    result.append([])
                result[level].append(node.val)

                if node.left:
                    list_aux.append((node.left, level + 1))
                if node.right:
                    list_aux.append((node.right, level + 1))

            queue, list_aux = list_aux, queue
            list_aux.clear()
        return result
