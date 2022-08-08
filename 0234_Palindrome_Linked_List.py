# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindromeStack(self, head: Optional[ListNode]) -> bool:
        # Runtime: 885 ms, faster than 84.87% of Python3 online submissions for Palindrome Linked List.
        # Memory Usage: 46.9 MB, less than 29.04% of Python3 online submissions for Palindrome Linked List.
        # Time: O(N)
        # Space: O(N)
        node = head
        size = 1
        while node.next:
            node = node.next
            size += 1
        stack = []
        node = head
        i = 0
        while i < size // 2:
            stack.append(node.val)
            i += 1
            node = node.next

        if size % 2 == 1:
            node = node.next

        while stack:
            node_val = stack.pop()
            if node_val != node.val:
                return False
            node = node.next
        return not stack and not node

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Time: O(N)
        # Space: O(1)
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        if fast:
            slow = slow.next
        while slow and prev:
            if not slow.val == prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return not slow and not prev

# Runtime: 1054 ms, faster than 68.03% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 31 MB, less than 99.70% of Python3 online submissions for Palindrome Linked List.
