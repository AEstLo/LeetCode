from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time: O(log M) + O(log N)
        # Space: O(log M) + O(log N)
        M = len(matrix)
        N = len(matrix[0])

        def matrixBinarySearch(l_row, r_row, l_col, r_col):
            if l_row <= r_row and l_col <= r_col:
                row = (l_row + r_row) // 2
                col = (l_col + r_col) // 2
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    return matrixBinarySearch(l_row, row - 1, l_col, r_col) or matrixBinarySearch(l_row, r_row, l_col, col - 1)
                else:
                    return matrixBinarySearch(row + 1, r_row, l_col, r_col) or matrixBinarySearch(l_row, r_row, col + 1, r_col)
            return False

        return matrixBinarySearch(0, M-1, 0, N-1)

# Runtime: 188 ms, faster than 84.94% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.8 MB, less than 6.31% of Python3 online submissions for Search a 2D Matrix II.
