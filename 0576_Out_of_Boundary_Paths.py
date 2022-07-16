class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        Time: without memoization -> O(4^maxMove)... with memoization -> O(m*n)
        Space: without memoization -> O(maxMove).... with memoization -> O(m*n*maxMove)
        """
        memo = {}
        MOD = 10**9 + 7

        def findPathsRecursive(remaining_moves, row, col):
            k = (remaining_moves, row, col)
            if k in memo:
                return memo[k]
            if not (1 <= row <= m) or not (1 <= col <= n):
                return 1
            if remaining_moves <= 0:
                return 0

            memo[k] = (findPathsRecursive(remaining_moves - 1, row - 1, col) + findPathsRecursive(remaining_moves - 1, row + 1, col) +
                       findPathsRecursive(remaining_moves - 1, row, col - 1) + findPathsRecursive(remaining_moves - 1, row, col + 1)) % MOD
            return memo[k]

        return findPathsRecursive(maxMove, startRow + 1, startColumn + 1)

# Runtime: 134 ms, faster than 82.35% of Python3 online submissions for Out of Boundary Paths.
# Memory Usage: 18.1 MB, less than 52.43% of Python3 online submissions for Out of Boundary Paths.
