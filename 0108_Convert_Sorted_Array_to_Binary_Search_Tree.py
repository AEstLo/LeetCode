# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Time: O(N)
        # Space: O(N)
        def recursion(left, right):
            if left > right:
                return None
            middle = left + (right - left) // 2
            node = TreeNode(nums[middle])
            node.left = recursion(left, middle - 1)
            node.right = recursion(middle + 1, right)
            return node
        root = recursion(0, len(nums) - 1)
        return root

# Runtime: 128 ms, faster than 52.36% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 15.6 MB, less than 83.29% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
