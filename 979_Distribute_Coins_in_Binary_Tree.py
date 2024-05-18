# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.sol = 0

        def rec(node):
            if node is None:
                return 0
            l_coins = rec(node.left)
            r_coins = rec(node.right)
            coins = node.val - 1 + l_coins + r_coins
            self.sol += abs(coins)
            return coins

        rec(root)
        return self.sol
