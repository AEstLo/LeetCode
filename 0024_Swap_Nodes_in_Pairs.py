# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Being N the number of nodes
        # Time: O(N)
        # Space: O(1)
        if not head:
            return head
        prev = None
        node = head
        next_node = node.next
        if next_node:
            head = next_node
        while next_node:
            node.next = next_node.next
            next_node.next = node
            if prev:
                prev.next = next_node
            prev = node
            node = node.next
            if node:
                next_node = node.next
            else:
                next_node = None
        return head
