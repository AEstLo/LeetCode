# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head.next
        while fast:
            slow = fast
            fast = fast.next
            while fast and fast.val > 0:
                slow.val += fast.val
                fast = fast.next
            fast = fast.next
            slow.next = fast
        return head.next
