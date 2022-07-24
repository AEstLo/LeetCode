class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time: O(n+m)
        # Space: O(1)
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

# Runtime: 56 ms, faster than 73.71% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.4 MB, less than 89.03% of Python3 online submissions for Search a 2D Matrix.
