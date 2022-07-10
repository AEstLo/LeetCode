# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Being N the number of nodes
        # Time: O(N)
        # Space: O(1)

        # sentinel -- This is an aux node to avoid edge cases
        sentinel = ListNode(0, head)

        prev = sentinel
        node = head
        while node:
            duplicated = False
            while node.next and node.val == node.next.val:
                node.next = node.next.next
                duplicated = True
            if duplicated:
                if prev:
                    prev.next = node.next
            else:
                prev = node
            node = node.next
        return sentinel.next
