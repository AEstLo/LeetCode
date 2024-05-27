# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        h = ListNode()
        prev = h
        while True:
            i = 1
            prev.next = node
            runner = node
            while i < k and runner:
                runner = runner.next
                i += 1
            if not runner:
                return h.next
            i = 1
            initial = node
            prev_node = node
            node = node.next
            while i < k:
                next_node = node.next
                node.next = prev_node
                prev_node = node
                node = next_node
                i += 1
            prev.next = prev_node
            prev = initial
