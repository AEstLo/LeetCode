from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {}

        def minFallingPathSumRecursive(row, col):
            if row + 1 == n:
                return matrix[row][col]
            if (row, col) in memo:
                return memo[(row, col)]
            values = []
            for next_col_val in range(-1, 2):
                if not (0 <= col + next_col_val < n):
                    continue
                values.append(minFallingPathSumRecursive(row + 1, col + next_col_val))
            memo[(row, col)] = min(values) + matrix[row][col]
            return memo[(row, col)]

        return min(minFallingPathSumRecursive(0, _col) for _col in range(n))
