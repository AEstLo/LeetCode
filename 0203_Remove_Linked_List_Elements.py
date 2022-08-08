# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Time: O(N)
        # Space: O(1)
        aux = ListNode(next=head)
        prev = aux
        node = head
        while node:
            if node.val == val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return aux.next

# Runtime: 123 ms, faster than 30.28% of Python3 online submissions for Remove Linked List Elements.
# Memory Usage: 17.8 MB, less than 81.81% of Python3 online submissions for Remove Linked List Elements.
