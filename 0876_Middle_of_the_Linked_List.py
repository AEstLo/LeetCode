# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = runner = head
        while runner and runner.next:
            node = node.next
            runner = runner.next.next
        return node

# Runtime: 43 ms, faster than 65.03% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.8 MB, less than 55.54% of Python3 online submissions for Middle of the Linked List.
