class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(grumpy)
        l = 0
        total = 0
        while l < n and grumpy[l] == 0:
            total += customers[l]
            l += 1
        max_value = 0
        r = l
        while r < n and r < l + minutes:
            if grumpy[r] == 1:
                max_value += customers[r]
            else:
                total += customers[r]
            r += 1
        minutes_used = max_value
        while r < n:
            if grumpy[l] == 1:
                max_value -= customers[l]
            if grumpy[r] == 1:
                max_value += customers[r]
            else:
                total += customers[r]
            minutes_used = max(minutes_used, max_value)
            l += 1
            r += 1
        return total + minutes_used
