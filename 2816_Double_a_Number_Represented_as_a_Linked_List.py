# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleItRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head.val *= 2
        if head.next is None:
            return
        self.doubleItRecursive(head.next)
        if head.next.val >= 10:
            head.next.val %= 10
            head.val += 1
        return

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(next=head)
        self.doubleItRecursive(node.next)
        if head.val >= 10:
            head.val %= 10
            node.val = 1
            return node
        return head
