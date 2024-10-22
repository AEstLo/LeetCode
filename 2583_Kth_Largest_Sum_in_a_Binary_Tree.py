# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        results = []
        q = deque([(1, root)])
        while q:
            level, node = q.pop()
            if level > len(results):
                results.append(0)
            results[level - 1] -= node.val
            if node.left:
                q.appendleft((level + 1, node.left))
            if node.right:
                q.appendleft((level + 1, node.right))
        
        heapq.heapify(results)
        while results and k - 1 > 0:
            heapq.heappop(results)
            k -= 1
        if not results:
            return -1

        return -results[0]
