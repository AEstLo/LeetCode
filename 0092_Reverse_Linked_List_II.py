# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Time: O(N)
        # Space: O(N)
        if left == right:
            return head
        node = head
        i = 1
        prev_left = None
        while node.next and i < left:
            prev_left = node
            node = node.next
            i += 1
        node_left = node

        stack = []

        while node and i <= right:
            stack.append(node)
            node = node.next
            i += 1

        next_right = node

        while stack:
            node = stack.pop()
            if not prev_left:
                head = node
            else:
                prev_left.next = node
            prev_left = node

        node.next = next_right
        return head

# Runtime: 31 ms, faster than 94.92% of Python3 online submissions for Reverse Linked List II.
# Memory Usage: 13.9 MB, less than 98.94% of Python3 online submissions for Reverse Linked List II.
