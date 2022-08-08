# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iteratively
        # Runtime: 39 ms, faster than 90.75% of Python3 online submissions for Reverse Linked List.
        # Memory Usage: 15.6 MB, less than 28.83% of Python3 online submissions for Reverse Linked List.
        # Time: O(N)
        # Space: O(1)
        prev = None
        node = head
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursively
        # 60 ms
        # 20.5 MB
        # Time: O(N)
        # Space: O(N) -- Stack of recursive calls
        new_head = None

        def recursive(node, next_node):
            if not next_node:
                nonlocal new_head
                new_head = node
                return
            recursive(next_node, next_node.next)
            next_node.next = node
        recursive(None, head)
        return new_head
