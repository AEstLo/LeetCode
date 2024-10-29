class Solution:
    def checkSquares(self, matrix, m, n, row, column, offset):
        if row >= m or column >= n or not matrix[row][column]:
            return False
        if offset < 1 and matrix[row][column]:
            return True
        if column + offset >= n or row + offset >= m:
            return False
        for r in range(row, row + offset + 1):
            if not matrix[r][column + offset]:
                return False
        for c in range(column, column + offset + 1):
            if not matrix[row + offset][c]:
                return False
        return True

    def countSquares(self, matrix: List[List[int]]) -> int:
        total = 0
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for column in range(n):
                offset = 0
                while self.checkSquares(matrix, m, n, row, column, offset):
                    total += 1
                    offset += 1
        return total
