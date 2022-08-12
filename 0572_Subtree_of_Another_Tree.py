# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def getIsSubtree(node, subNode):
            if node and subNode:
                return node.val == subNode.val and getIsSubtree(node.left, subNode.left) and getIsSubtree(node.right, subNode.right)
            return node is subNode

        if not root:
            return False
        if getIsSubtree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

# Runtime: 183 ms, faster than 54.78% of Python3 online submissions for Subtree of Another Tree.
# Memory Usage: 15.2 MB, less than 35.59% of Python3 online submissions for Subtree of Another Tree.
