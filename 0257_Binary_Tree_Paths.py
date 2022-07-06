# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        raw_result = self.binaryTreePathsDFS(root)
        result = []
        for res in raw_result:
            result.append('->'.join(res))
        return result

    def binaryTreePathsDFS(self, root: Optional[TreeNode]) -> List[str]:
        ret = []
        if root is not None:
            aux = [str(root.val)]
            left = self.binaryTreePathsDFS(root.left)
            for l in left:
                ret.append(aux + l)
            right = self.binaryTreePathsDFS(root.right)
            for r in right:
                ret.append(aux + r)
            if not ret:
                ret.append(aux)
        return ret
