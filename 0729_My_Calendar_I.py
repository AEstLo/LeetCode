class MyCalendar:

    def __init__(self):
        self.calendar = {}

    def book(self, start: int, end: int) -> bool:
        # Being B the number of bookins of the calendar
        # Time: O(B^2)
        # Space: O(B)
        for k, v in self.calendar.items():
            if not ((start < k and end <= k) or (start >= v and end > v)):
                return False
        self.calendar[start] = end
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# Runtime: 1379 ms, faster than 14.88% of Python3 online submissions for My Calendar I.
# Memory Usage: 14.7 MB, less than 92.29% of Python3 online submissions for My Calendar I.
