from typing import List, Optional


class TreeNode:  # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorder(self):
        result = []

        def preorderRecursive(node):
            if node:
                result.append(node.val)
                preorderRecursive(node.left)
                preorderRecursive(node.right)

        preorderRecursive(self)
        return result

    def inorder(self):
        result = []

        def inorderRecursive(node):
            if node:
                inorderRecursive(node.left)
                result.append(node.val)
                inorderRecursive(node.right)

        inorderRecursive(self)
        return result


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Time: O(N)
        Space: O(N)
        """
        map_val_pos_inorder = {val: idx for idx, val in enumerate(inorder)}

        preorder_index = 0

        def process(left, right):
            """
            preorder = root, left_preorder, right_preorder
            inorder = left_inorder, root, right_inorder

            So, if I know where the next root is, I can build the tree from the inorder recursively.
            """
            if left > right:
                return None

            nonlocal preorder_index

            value = preorder[preorder_index]
            preorder_index += 1
            node = TreeNode(value)

            node.left = process(left, map_val_pos_inorder[value] - 1)
            node.right = process(map_val_pos_inorder[value] + 1, right)

            return node

        return process(0, len(preorder) - 1)


s = Solution()
preorder_list = [3, 9, 20, 15, 7]
inorder_list = [9, 3, 15, 20, 7]
r = s.buildTree(preorder_list, inorder_list)
print(r.preorder(), preorder_list)
print(r.inorder(), inorder_list)

preorder_list = [1, 2, 3, 4]
inorder_list = [4, 3, 2, 1]
r = s.buildTree(preorder_list, inorder_list)
print(r.preorder(), preorder_list)
print(r.inorder(), inorder_list)
