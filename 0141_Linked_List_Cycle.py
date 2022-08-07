# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time: O(N)
        # Space: O(1)
        node = runner = head
        while runner:
            if not runner.next:
                return False
            node = node.next
            runner = runner.next.next
            if node == runner:
                return True
        return False

# Runtime: 88 ms, faster than 48.92% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.6 MB, less than 31.17% of Python3 online submissions for Linked List Cycle.
