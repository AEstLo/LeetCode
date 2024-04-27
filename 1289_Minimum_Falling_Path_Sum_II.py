from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = {}

        def minFallingPathSumRecursive(row, col):
            if row + 1 == n:
                return grid[row][col]
            if (row, col) in memo:
                return memo[(row, col)]
            values = []
            for next_col in range(n):
                if next_col == col:
                    continue
                values.append(minFallingPathSumRecursive(row + 1, next_col))
            memo[(row, col)] = min(values) + grid[row][col]
            return memo[(row, col)]

        return min(minFallingPathSumRecursive(0, _col) for _col in range(n))
