class Solution:
    def climbStairs2(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs(self, n: int) -> int:
        memo = {}

        def recursiveClimbStairs(pos):
            if pos <= 2:
                return pos
            if pos in memo:
                return memo[pos]
            memo[pos] = recursiveClimbStairs(
                pos - 1) + recursiveClimbStairs(pos - 2)
            return memo[pos]
        return recursiveClimbStairs(n)
