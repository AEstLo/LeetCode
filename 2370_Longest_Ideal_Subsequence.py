class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # DP
        S = len(s)
        dp = [0] * 26
        ord_a = ord('a')
        for i in range(S):
            idx = ord(s[i]) - ord_a
            longest = -1
            for j in range(26):
                if abs(idx - j) <= k:
                    longest = max(
                        dp[j] + 1,
                        longest,
                    )
            if longest > dp[idx]:
                dp[idx] = longest
        return max(dp)

        # Memoization
        S = len(s)
        memo = {}

        def helper(i, prev_i=-1):
            # base case
            if i >= S:
                return 0
            if (i, prev_i) in memo:
                return memo[(i, prev_i)]

            # skip character
            result = helper(i + 1, prev_i)
            # select character
            if prev_i < 0 or abs(ord(s[i]) - ord(s[prev_i])) <= k:
                result = max(
                    result,
                    1 + helper(i + 1, i)
                )
            memo[(i, prev_i)] = result
            return result

        return helper(0)
