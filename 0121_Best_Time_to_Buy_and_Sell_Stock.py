class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(N)
        # Space: O(N)
        # Using a monothonic stack
        stack = []
        profit = 0
        for price in prices:
            while stack and stack[-1] >= price:
                old_price = stack.pop()
                if stack:
                    profit = max(profit, old_price - stack[0])
            stack.append(price)
        while stack:
            old_price = stack.pop()
            if stack:
                profit = max(profit, old_price - stack[0])
        return profit

# Runtime: 1184 ms, faster than 83.45% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25 MB, less than 38.44% of Python3 online submissions for Best Time to Buy and Sell Stock.
