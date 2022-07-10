from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Time: O(N)
        # Space: O(N)
        N = len(cost)
        dp = [-1] * N
        dp[N - 1] = cost[N - 1]
        dp[N - 2] = cost[N - 2]
        for i in range(N - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])
