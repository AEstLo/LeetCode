class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Time: O(total_days * 3) = O(total_days)
        # Space: O(total_days * 3) = O(total_days)
        total_days = len(days)

        memo = {}

        def mincostTicketsRecursive(index, valid_until):
            k = (index, valid_until)
            if k in memo:
                return memo[k]
            i = index
            while i < total_days and days[i] < valid_until:
                i += 1

            if i >= total_days:
                return 0

            memo[k] = min(
                mincostTicketsRecursive(i, days[i] + 1) + costs[0],
                mincostTicketsRecursive(i, days[i] + 7) + costs[1],
                mincostTicketsRecursive(i, days[i] + 30) + costs[2],
            )
            return memo[k]

        return mincostTicketsRecursive(0, 0)

# Runtime: 70 ms, faster than 56.43% of Python3 online submissions for Minimum Cost For Tickets.
# Memory Usage: 14.9 MB, less than 14.69% of Python3 online submissions for Minimum Cost For Tickets.
