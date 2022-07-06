# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n) -- being n the number of nodes of the longest linked list
        # Space: O(n) -- being n the number of nodes of the longest linked list
        head = ListNode()
        result_node = head
        node1 = l1
        node2 = l2
        carry = 0
        while node1 or node2:
            if node1:
                result_node.val += node1.val
                node1 = node1.next
            if node2:
                result_node.val += node2.val
                node2 = node2.next
            carry = result_node.val // 10
            result_node.val %= 10
            if node1 or node2 or carry > 0:
                result_node.next = ListNode(carry)
                result_node = result_node.next
        return head
