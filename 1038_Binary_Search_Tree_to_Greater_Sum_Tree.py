# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def bstToGstRec(node, value):
            if not node:
                return None
            left_most = bstToGstRec(node.right, value)
            if left_most:
                node.val += left_most.val
            else:
                node.val += value
            if node.left:
                return bstToGstRec(node.left, node.val)
            return node

        bstToGstRec(root, 0)
        return root
            
