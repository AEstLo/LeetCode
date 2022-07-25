class Solution:
    def countBits(self, n: int) -> List[int]:
        # Time: O(N)
        # Space: O(N)
        dp = [0] * (n + 1)
        current_base = 1
        i = 1
        while i < n+1:
            dp[i] = 1 + dp[i % current_base]
            i += 1
            if i >= current_base * 2:
                current_base *= 2
        return dp

# Runtime: 89 ms, faster than 90.44% of Python3 online submissions for Counting Bits.
# Memory Usage: 20.7 MB, less than 78.91% of Python3 online submissions for Counting Bits.
