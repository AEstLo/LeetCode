# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        node = head.next
        stack = [head]
        while node:
            while stack and stack[-1].val < node.val:
                stack.pop()
            if stack:
                stack[-1].next = node
            stack.append(node)
            node = node.next
        return stack[0]
