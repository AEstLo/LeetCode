# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Being m the number of nodes of the linked list
        # Time: O(m)
        # Space: O(1)
        node = head
        runner = head
        i = 1
        while i <= n and runner:
            runner = runner.next
            i += 1

        if not runner:
            if i <= n:
                return head
            i -= 1
            if i <= n:
                return head.next
            return None

        while runner.next:
            runner = runner.next
            node = node.next

        node.next = node.next.next
        return head
