class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time: O(m * n)
        # Space: O(m * n)
        memo = {}

        def getUniquePaths(row, col):
            if row >= m or col >= n:
                return 0
            if row == m - 1 and col == n - 1:
                return 1
            key = f'{row},{col}'
            if key in memo:
                return memo[key]
            memo[key] = getUniquePaths(
                row + 1, col) + getUniquePaths(row, col + 1)
            return memo[key]
        return getUniquePaths(0, 0)
