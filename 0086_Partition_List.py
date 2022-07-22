# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Time: O(N)
        # Space: O(1)
        less_pre_head = ListNode(val=0)
        equal_greater_pre_head = ListNode(val=0)
        node = head
        less_node = less_pre_head
        equal_greater_node = equal_greater_pre_head
        while node:
            if node.val < x:
                less_node.next = node
                less_node = node
            else:
                equal_greater_node.next = node
                equal_greater_node = node
            node = node.next
        equal_greater_node.next = None
        less_node.next = equal_greater_pre_head.next

        return less_pre_head.next

# Runtime: 56 ms, faster than 44.95% of Python3 online submissions for Partition List.
# Memory Usage: 13.9 MB, less than 31.57% of Python3 online submissions for Partition List.
