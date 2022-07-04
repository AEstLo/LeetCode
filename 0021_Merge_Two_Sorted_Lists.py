# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        node1 = list1
        node2 = list2
        
        if node1.val <= node2.val:
            head = node1
            node1 = node1.next
        else:
            head = node2
            node2 = node2.next
        
        node = head
        while node1 and node2:
            if node1.val <= node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next
        while node1:
            node.next = node1
            node = node.next
            node1 = node1.next
        while node2:
            node.next = node2
            node = node.next
            node2 = node2.next
        
        return head
