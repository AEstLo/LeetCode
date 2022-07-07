# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        # Being N the number of nodes
        # Time: O(N)
        # Space: O(N)
        if not root:
            self.root = None
            return
        x = 0
        root.val = 0
        queue = [root]
        queue2 = []
        while queue:
            for node in queue:
                x = node.val
                if node.left :
                    node.left.val = 2 * x + 1
                    queue2.append(node.left)
                if node.right:
                    node.right.val = 2 * x + 2
                    queue2.append(node.right)
            queue, queue2 = queue2, queue
            queue2.clear()
        self.root = root

    def find(self, target: int) -> bool:
        # Being N the number of nodes
        # Time: O(logN)
        # Space: O(logN)
        stack = []
        while target > 0:
            if target % 2 == 0:
                target = (target - 2) // 2
                stack.append('r')
            else:
                target = (target - 1) // 2
                stack.append('l')
        node = self.root
        while stack:
            direction = stack.pop()
            if direction == 'l':
                node = node.left
            else:
                node = node.right
            if not node:
                return False
        return True if node else False



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
