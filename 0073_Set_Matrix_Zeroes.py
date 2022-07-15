class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Time: O(M * N)
        # Space: O(M + N)
        M = len(matrix)
        N = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        for row in range(M):
            for col in range(N):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)
        for row in zero_rows:
            for col in range(N):
                matrix[row][col] = 0
        for col in zero_cols:
            for row in range(M):
                matrix[row][col] = 0
        return
